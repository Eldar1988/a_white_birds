import requests
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import ServiceContactResumeForm, RequestForm
from .models import Service, ServiceInfo, SubService
from ..main.models import TelegramBot


def get_bot():
    bot = TelegramBot.objects.last()
    return bot


def get_bot_url(request_mode, bot):
    url = f'{bot.url}' + f'{request_mode}'
    return url


def get_bot_chat_id(bot):
    chat_id = bot.chat_id
    return chat_id


def service_list(request):
    """Список услуг"""
    service_info = ServiceInfo.objects.last()
    service = Service.objects.order_by('number')
    service_info_seo = service_info.text[3:160]

    return render(request, 'service/service_list.html', {
        'service': service,
        'service_info': service_info,
        'service_info_seo': service_info_seo,
    })


class ServiceDetail(View):
    """Детали услуги"""
    def get(self, request, pk):
        service = Service.objects.get(id=pk)
        service_seo = service.description[3:160]

        return render(request, 'service/service_detail.html', {
            'service': service,
            'service_seo': service_seo,
        })


class SubServiceDetail(View):
    """Детали услуги"""
    def get(self, request, pk):
        service = SubService.objects.get(id=pk)
        service_seo = service.description[3:160]
        form = ServiceContactResumeForm

        return render(request, 'service/subservice_detail.html', {
            'service': service,
            'service_seo': service_seo,
            'form': form,
        })


class AddNewResume(View):
    """Новое резюме"""
    def post(self, request):
        form = ServiceContactResumeForm(request.POST, request.FILES)
        id = request.POST.get('id')

        if form.is_valid():
            form.save()
            title = request.POST.get('title')
            bot = get_bot()
            url = get_bot_url('sendMessage', bot)
            chat_id = get_bot_chat_id(bot)

            text = f'Новое резюме было создано пользователем на странице услуги: \n {title}'
            answer = {'chat_id': chat_id, 'text': text}
            requests.post(url, answer)

        return redirect('subservice_detail', id)


class AddContactRequest(View):
    """Новая заявка на услугу"""
    def post(self, request):
        form = RequestForm(request.POST)
        id = request.POST.get('id')

        if form.is_valid():
            form.save()

            title = request.POST.get('service')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            comment = request.POST.get('comment')
            bot = get_bot()
            url = get_bot_url('sendMessage', bot)
            chat_id = get_bot_chat_id(bot)

            text = f'Новая заявка на услугу: \n\n Услуга: {title} \n Имя: {name} \n Телефон: {phone} \n Дополнительно: {comment}'
            answer = {'chat_id': chat_id, 'text': text}
            requests.post(url, answer)

        return redirect('subservice_detail', id)
