from django.contrib.auth.models import User
from django.db import models
from HelloDjango.settings import path_and_rename


class Profile(models.Model):
    """Профиль соискателя"""
    name = models.CharField('Наименование профиля', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Sphere(models.Model):
    """Сфера деятельности соискателя"""
    name = models.CharField('Наименование сферы', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сфера'
        verbose_name_plural = 'Сферы'


class Experience(models.Model):
    """Опыт работы соискателя"""
    name = models.CharField('Опыт работы', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class WorkRequest(models.Model):
    """Запрос соискателя"""
    name = models.CharField('Запрос соискателя', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'


class HhRequest(models.Model):
    """Заявка от соискателя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User, verbose_name='Пользователь')
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name='Профиль')
    sphere = models.ForeignKey(Sphere, on_delete=models.PROTECT, verbose_name='Сфера')
    experience = models.ForeignKey(Experience, on_delete=models.PROTECT, verbose_name='Опыт работы')
    work_request = models.ForeignKey(WorkRequest, on_delete=models.PROTECT, verbose_name='Запрос')
    resume = models.FileField('Резюме', upload_to=path_and_rename("hhfiles/", 'resume'))
    email = models.EmailField('Email', null=True)
    pub_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Запрос на уведомления'
        verbose_name_plural = 'Запросы на уведомления'

