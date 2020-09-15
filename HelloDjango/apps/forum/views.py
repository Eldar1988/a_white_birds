import requests
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import ForumNewParticipantForm
from .models import ForumInfo, ForumParticipant, Facilitator, InfoBlock, ForumPartner, ForumParticipant2020, \
    Facilitator2020

from ..main.models import TelegramBot


def get_bot():
    bot = TelegramBot.objects.get(number=1)
    return bot


def get_bot_url(request_mode, bot):
    url = f'{bot.url}' + f'{request_mode}'
    return url


def get_bot_chat_id(bot):
    chat_id = bot.chat_id
    return chat_id


class ForumView(View):
    def get(self, request):
        #  Общая информация о форуме
        forum_info = ForumInfo.objects.last()
        info_block = InfoBlock.objects.order_by('order')
        forum_partners = ForumPartner.objects.all()

        #  Участники 2019
        first_table_participants = ForumParticipant.objects.filter(table=1)
        second_table_participants = ForumParticipant.objects.filter(table=2)
        third_table_participants = ForumParticipant.objects.filter(table=3)
        fourth_table_participants = ForumParticipant.objects.filter(table=4)

        #  Участники 2020
        first_table_participants2020 = ForumParticipant2020.objects.filter(table=1)
        second_table_participants2020 = ForumParticipant2020.objects.filter(table=2)
        third_table_participants2020 = ForumParticipant2020.objects.filter(table=3)
        fourth_table_participants2020 = ForumParticipant2020.objects.filter(table=4)

        #  Фасилитаторы 2019
        first_table_facilitator = Facilitator.objects.filter(table=1)
        second_table_facilitator = Facilitator.objects.filter(table=2)
        third_table_facilitator = Facilitator.objects.filter(table=3)
        fourth_table_facilitator = Facilitator.objects.filter(table=4)
        special = Facilitator.objects.filter(table=5)

        #  Фасилитаторы 2020
        first_table_facilitator2020 = Facilitator2020.objects.filter(table=1)
        second_table_facilitator2020 = Facilitator2020.objects.filter(table=2)
        third_table_facilitator2020 = Facilitator2020.objects.filter(table=3)
        fourth_table_facilitator2020 = Facilitator2020.objects.filter(table=4)

        return render(request, 'forum/forum.html', {
            'forum_info': forum_info,
            'info_block': info_block,
            'forum_partners': forum_partners,

            'first_table_participants': first_table_participants,
            'second_table_participants': second_table_participants,
            'third_table_participants': third_table_participants,
            'fourth_table_participants': fourth_table_participants,

            'first_table_participants2020': first_table_participants2020,
            'second_table_participants2020': second_table_participants2020,
            'third_table_participants2020': third_table_participants2020,
            'fourth_table_participants2020': fourth_table_participants2020,

            'first_table_facilitator': first_table_facilitator,
            'second_table_facilitator': second_table_facilitator,
            'third_table_facilitator': third_table_facilitator,
            'fourth_table_facilitator': fourth_table_facilitator,

            'first_table_facilitator2020': first_table_facilitator2020,
            'second_table_facilitator2020': second_table_facilitator2020,
            'third_table_facilitator2020': third_table_facilitator2020,
            'fourth_table_facilitator2020': fourth_table_facilitator2020,

            'special': special,
        })

    def post(self, request):
        form = ForumNewParticipantForm(request.POST)
        if form.is_valid():
            #  Отправляем данные в телеграм
            bot = get_bot()
            url = get_bot_url('sendMessage', bot)
            chat_id = get_bot_chat_id(bot)
            name = request.POST.get('name')
            company = request.POST.get('company')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            text = f'Новая заявка на учатсие в форуме ' \
                   f'\nИмя: {name} ' \
                   f'\nКомпания: {company} ' \
                   f'\nТелефон: {phone} ' \
                   f'\nEmail: {email}'
            answer = {'chat_id': chat_id, 'text': text}
            requests.post(url, answer)

            # Сохраняем форму
            form.save()
            return redirect('forum')
