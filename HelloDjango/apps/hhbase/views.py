from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import WorkRequestForm
from .models import HhRequest, Profile, Experience, Sphere, WorkRequest
from ..main.models import TelegramBot

import requests


def get_bot():
    bot = TelegramBot.objects.get(number=1)
    return bot


def get_bot_url(request_mode, bot):
    url = f'{bot.url}' + f'{request_mode}'
    return url


def get_bot_chat_id(bot):
    chat_id = bot.chat_id
    return chat_id


class WorkRequestobjects(object):
    pass


class AddRequestView(View):
    """Создание заявки на уведомления о вакансиях"""
    def post(self, request):
        form = WorkRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.email = request.user.email
            form.save()

            #  Отправляем данные в телеграм
            bot = get_bot()
            url = get_bot_url('sendMessage', bot)
            chat_id = get_bot_chat_id(bot)
            profile = Profile.objects.get(id=request.POST.get('profile')).name
            experience = Experience.objects.get(id=request.POST.get('experience')).name
            sphere = Sphere.objects.get(id=request.POST.get('sphere')).name
            work_request = WorkRequest.objects.get(id=request.POST.get('work_request')).name
            user = request.user
            hh_request = HhRequest.objects.get(user=user)
            resume = f'https://whitebirds.kz/media/{hh_request.resume}'
            text = f'Новая заявка на уведомления о вакансиях ' \
                   f'\nПрофиль: {profile} ' \
                   f'\nСфера: {sphere} ' \
                   f'\nОпыт: {experience} ' \
                   f'\nЗапрос: {work_request}' \
                   f'\nРезюме: {resume}'
            answer = {'chat_id': chat_id, 'text': text}
            requests.post(url, answer)

        return redirect('profile')