from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from HelloDjango.settings import path_and_rename



class ServiceInfo(models.Model):
    """Общая информация"""
    title = models.CharField('Заголовок страницы со списком услуг', max_length=255, blank=True, null=True)
    text = RichTextUploadingField('Дополнительная информация на странице со списком услуг', blank=True, null=True)
    image = models.ImageField('Картинка на странице услуг', upload_to=path_and_rename("service/", 'image'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуги - общая информация'
        verbose_name_plural = 'Услуги - общая информация'


class SubService(models.Model):
    """Раздел услуги"""
    title = models.CharField('Заголовок', max_length=255)
    description = RichTextUploadingField('Описание услуги')
    form = models.BooleanField('Форма заявки', default=False)
    form_resume = models.BooleanField('Форма с резюме', default=False)
    program = models.FileField('Программа (файл PDF)', upload_to=path_and_rename("service/", 'image'), null=True, blank=True)
    presentation_text = models.TextField('Текст, предлагающий скачать программу или презентацию', default='Ознакомиться с программой')
    btn_text = models.CharField('Текст на кнопке скачивания программы', default='Скачать', max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subservice_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Дополнительно - услуга'
        verbose_name_plural = 'Дополнительно - услуги'


class Service(models.Model):
    """Услуга"""
    number = models.PositiveSmallIntegerField('Номер', null=True, blank=True)
    image = models.ImageField('Картинка услуги', upload_to=path_and_rename("service/", 'image'))
    title = models.CharField('Заголовок - название услуги', max_length=255)
    description = RichTextUploadingField('Описание услуги')
    sub_service = models.ManyToManyField(SubService, verbose_name='Дополнительные услуги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServiceContact(models.Model):
    """Заявка на консультацию"""
    service = models.CharField('Услуга', max_length=255, null=True, blank=True)
    name = models.CharField('Имя', max_length=200)
    phone = models.CharField('Телефон', max_length=50)
    comment = models.TextField('Дополнительно')

    def __str__(self):
        return f"{self.name} {self.service}"

    class Meta:
        verbose_name = 'Заявка на услугу'
        verbose_name_plural = 'Заявки на услуги'


class Profile(models.Model):
    """Профиль для резюме"""
    title = models.CharField('Название профиля', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профиль для резюме'
        verbose_name_plural = 'Профили для резюме'


class Sphere(models.Model):
    """Сфера для резюме"""
    title = models.CharField('Название сферы', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сфера для резюме'
        verbose_name_plural = 'Сферы для резюме'


class Experience(models.Model):
    """Опыт роаботы для резюме"""
    title = models.CharField('Вариант', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опыт работы для резюме'
        verbose_name_plural = 'Опыт работы для резюме'


class SelfRequest(models.Model):
    """Опыт роаботы для резюме"""
    title = models.CharField('Запрос', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запрос для резюме'
        verbose_name_plural = 'Запросы для резюме'


class ServiceContactResume(models.Model):
    """Заявка резюме"""
    name = models.CharField('ФИО', max_length=255)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=30)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Профиль')
    sphere = models.ForeignKey(Sphere, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сфера')
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Опыт работы')
    self_request = models.ForeignKey(SelfRequest, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Запрос')
    resume = models.FileField('Файл', upload_to=path_and_rename("service_files/", 'resume'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
