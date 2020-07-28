from django.shortcuts import render, redirect

from django.views.generic.base import View

from .forms import WorkRequestForm


class AddRequestView(View):
    """Создание заявки на уведомления о вакансиях"""
    def post(self, request):
        form = WorkRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.email = request.user.email
            form.save()

        return redirect('profile')