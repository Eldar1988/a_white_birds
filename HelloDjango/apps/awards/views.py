from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import AwardRequestForm, JuryApprovedForm, AwardNewParticipantForm
from .models import AwardInfo, AwardsIconBlock, Request, NominationJury, Profile


class AwardView(View):
    """Страница премии"""
    def get(self, request):
        award = AwardInfo.objects.last()
        icon_block = AwardsIconBlock.objects.all()
        jurys = Profile.objects.filter(jury=True)
        form = AwardNewParticipantForm

        return render(request, 'awards/award.html', {
            'award': award,
            'icon_block': icon_block,
            'jurys': jurys,
            'form': form,
            })

    def post(self, request):
        form = AwardNewParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('award')


class ProfileView(View):
    """Страница участника премии"""
    def get(self, request):
        user = request.user
        try:
            if user.profile.partisipant:
                try:
                    award_request = Request.objects.get(user=request.user)
                    return render(request, 'awards/award_user_profile.html', {
                        'award_request': award_request,
                        'user': user,
                    })

                except ObjectDoesNotExist:
                    form = AwardRequestForm
                    return render(request, 'awards/award_user_profile.html', {
                        'user': user,
                        'form': form,
                        })

            if user.profile.jury:
                message = True
                try:
                    award_request = Request.objects.filter(public_for_jury=True).exclude(jury_approved__name=user.first_name)
                    return render(request, 'awards/award_jury_profile.html', {
                        'award_request': award_request,
                        'user': user,
                    })

                except ObjectDoesNotExist:
                    return render(request, 'awards/award_user_profile.html', {
                        'user': user,
                        'message': message,
                        })
        except ObjectDoesNotExist:
            return render(request, 'awards/user_profile.html', {'user': user})


class AddRequestView(View):
    """Создание заявки на участие"""
    def post(self, request):
        form = AwardRequestForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('profile')

        else:
            return render(request, 'awards/form_error.html', {'form': form})


class RegisterView(View):
    """Регистрация нового пользователя"""
    def post(self, request):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        new_user = User.objects.create_user(username, email, password, first_name=first_name)
        new_user.save()
        message = 'message'
        return redirect(f"/accounts/login/?next={message}")


class RequestDetailView(View):
    """Детали заявки"""
    def get(self, request, pk):
        award_request = Request.objects.get(id=pk)
        nominations = NominationJury.objects.all()
        have_jury_vote = True

        # Проверяем на наличие оценки от жюри
        for i in award_request.jury_approved.all():
            if i.name == request.user.first_name:
                have_jury_vote = False

        # Проверяем на нличие голсоа от пользователя
        have_vote = 0
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        for i in award_request.vote.all():
            if i.ip == ip:
                have_vote = 1

        return render(request, 'awards/request_detail.html', {
            'have_jury_vote': have_jury_vote,
            'award_request': award_request,
            'nominations': nominations,
            'have_vote': have_vote,
        })


class AddJuryApprovedView(View):
    """Добавление оценки жюри"""
    def post(self, request, pk):
        form = JuryApprovedForm(request.POST)
        if request.POST.get('approved')=='on':
            approved_val = True
        else:
            approved_val = False

        if form.is_valid():
            request_self = Request.objects.get(id=pk)
            request_self.jury_approved.create(
                name=request.user.first_name,
                project=request.POST.get('project'),
                approved=approved_val,
                recommendation=request.POST.get('recommendation'),
                vote=request.POST.get('vote'),
                nomination_jury_id=request.POST.get('nomination_jury'),
            )
            return redirect('profile')


class AddVoteView(View):
    """Добавление голоса"""
    def get(self, request, pk):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        award_request = Request.objects.get(id=pk)

        if not award_request.vote.count():
            award_request.vote.create(
                ip=ip,
            )
        else:
            for i in award_request.vote.all():
                if i.ip != ip:
                    award_request.vote.create(
                        ip=ip,
                    )

        return redirect('request_detail', f"{pk}")


class AwardDetailView(View):
    """Детализация премии - Список"""
    def get(self, request):
        award_request = Request.objects.all()
        jury = Profile.objects.filter(jury=True)

        return render(request, 'awards/award_detail.html', {
            'award_request': award_request,
            'jury': jury,
        })


class RequestSelfDetailView(View):
    """Детализация премии - заявка"""
    def get(self, request, pk):
        award_request = Request.objects.get(id=pk)
        jury = Profile.objects.filter(jury=True)
        y = award_request.jury_approved.aggregate(Sum('vote'))  # Получаем общую сумму баллов оценок
        y = y['vote__sum']
        sr_ar = 'Не определено'
        if y is not None:
            sr_ar = y // award_request.jury_approved.all().count()
        a = award_request.vote.count()

        return render(request, 'awards/self_award_detail.html', {
            'award_request': award_request,
            'jury': jury,
            'sr_ar': sr_ar,
            'a': a,
        })
