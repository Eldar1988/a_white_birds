from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class MainInfo(models.Model):
    """Основная информация о компании"""
    name = models.CharField('Название компании', max_length=100)
    logo = models.ImageField('Логотип компании', upload_to='images/')
    phone = models.CharField('Телефон', max_length=100)
    address = models.TextField('Адрес компании')
    copyright = models.TextField('Копирайт', help_text='Будет расположен в футере')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Основная информация о компании'
        verbose_name_plural = 'Основная информация о компании'


class TelegramBot(models.Model):
    """Телеграм бот"""
    number = models.PositiveSmallIntegerField('Номер бота')
    purpose = models.CharField('Предназначение', max_length=200)
    url = models.URLField('URL', help_text='https://api.telegram.org/bot<bot_token>')
    chat_id = models.CharField('Caht ID', max_length=20)

    def __str__(self):
        return self.purpose

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'
