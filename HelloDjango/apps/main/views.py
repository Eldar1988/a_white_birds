from django.shortcuts import render
from django.views.generic.base import View
from .models import MainInfo


class MainInfoView(View):
    """Главная страница"""
    def get(self, request):
        main = MainInfo.objects.last()
        return render(request, 'main/index.html', {
            'main': main
        })


class ContactView(View):
    def get(self, request):
        contact = MainInfo.objects.last()

        return render(request, 'main/contacts.html', {
            'contact': contact,
        })
