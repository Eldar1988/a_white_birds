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
