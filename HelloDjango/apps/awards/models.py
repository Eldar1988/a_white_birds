from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

from .functions import path_and_rename


class AwardsIconBlock(models.Model):
    """Блок с иконками в описании премии"""
    title = models.CharField('Блок с иконкой - заголовок', max_length=200)
    description = models.TextField('Блок с иконкой - Описание')
    icon = models.CharField('Иконка', max_length=200,
                            help_text='Скопируйте иконку с сайта https://www.icofont.com/icons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок с иконкой (Премия)'
        verbose_name_plural = 'Блоки с иконкой (Премия)'


class FirstIcons(models.Model):
    """Блок с иконками в описании Участия"""
    title = models.CharField('Блок с иконкой - заголовок', max_length=200)
    description = models.TextField('Блок с иконкой - Описание')
    icon = models.CharField('Иконка', max_length=200,
                            help_text='Скопируйте иконку с сайта https://www.icofont.com/icons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок с иконкой - Участие (Премия)'
        verbose_name_plural = 'Блоки с иконкой - Участие (Премия)'


class SecondIcons(models.Model):
    """Блок с иконками в описании Голосование 1"""
    title = models.CharField('Блок с иконкой - заголовок', max_length=200)
    description = models.TextField('Блок с иконкой - Описание')
    icon = models.CharField('Иконка', max_length=200,
                            help_text='Скопируйте иконку с сайта https://www.icofont.com/icons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок с иконкой голсование 1 - Участие (Премия)'
        verbose_name_plural = 'Блоки с иконкой голосование 1 - Участие (Премия)'


class ThreeIcons(models.Model):
    """Блок с иконками в описании Голосование 2"""
    title = models.CharField('Блок с иконкой - заголовок', max_length=200)
    description = models.TextField('Блок с иконкой - Описание')
    icon = models.CharField('Иконка', max_length=200,
                            help_text='Скопируйте иконку с сайта https://www.icofont.com/icons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок с иконкой голсование 2 - Участие (Премия)'
        verbose_name_plural = 'Блоки с иконкой голосование 2 - Участие (Премия)'


class AwardInfo(models.Model):
    """Информация о премии"""
    award_title = models.CharField('Блок премия - заголовок', max_length=200)
    award_description = RichTextUploadingField('Блок премия - описание')
    award_image = models.ImageField('Блок премия - картинка', upload_to=path_and_rename("site/", 'image'),
                              help_text='не забудьте оптимизировать картинку на сайте https://tinypng.com/')

    jury_title = models.CharField('Блок жюри - заголовок', max_length=200)
    jury_description = RichTextUploadingField('Блок жюри - описание')
    involvement_title = models.CharField('Блок участие - заголовок', max_length=200)
    involvement_description = RichTextUploadingField('Блок участие - описание')
    votes_description = RichTextUploadingField('Блок голосование - описание (заголовок 3 уровня)', blank=True, null=True)
    votes_description_second = RichTextUploadingField('Блок голосование 2 - описание (заголовок 3 уровня)', blank=True, null=True)

    def __str__(self):
        return self.award_title

    class Meta:
        verbose_name = 'Премия общая информация'
        verbose_name_plural = 'Премия общая информация'


class Nomination(models.Model):
    name = models.CharField('Название номинации', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Номинация'
        verbose_name_plural = 'Номинации'


class NominationJury(models.Model):
    name = models.CharField('Название номинации к рекомендации', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Номинация от жюри'
        verbose_name_plural = 'Номинации от жюри'


class Vote(models.Model):
    """Голос"""
    ip = models.GenericIPAddressField('ip голосующего')

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = "Голоса"


class JuryApproved(models.Model):
    """Мнение жюри"""
    name = models.CharField('Имя жюри', max_length=200, blank=True)
    project = models.CharField('Проект', max_length=200, blank=True)
    approved = models.BooleanField('Одобрено', default=False)
    recommendation = models.TextField('Рекоммендации', blank=True)
    vote = models.SmallIntegerField('Оценка', blank=True, null=True)
    nomination_jury = models.ForeignKey(NominationJury, on_delete=models.SET_NULL, null=True,
                                        verbose_name='Рекомендация к номинации', blank=True)
    date = models.DateTimeField('Дата создания рекомендации', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мнение жюри'
        verbose_name_plural = 'Мнения жюри'


class Request(models.Model):
    """Заявка на участие"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь на сайте',
                                blank=True, null=True)
    name = models.CharField('ФИО', max_length=200)
    avatar = models.ImageField('Ваша фотография', blank=True, null=True,
                               upload_to=path_and_rename("award_files/avatars/", 'avatar'))
    company = models.CharField('Компания', max_length=200)
    professional = models.CharField('Должность', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=30)
    nomination = models.ForeignKey(Nomination, on_delete=models.PROTECT, verbose_name='Номинация')
    project_name = models.CharField('Название проекта', max_length=300)
    project_start_date = models.DateField('Дата внедрения проекта', default=timezone.now)
    project_appoints = RichTextUploadingField('Преимущества проекта', null=True)
    description = RichTextUploadingField('Описание проекта', null=True)
    results = RichTextUploadingField('Результаты, полученные после внедрения проекта', null=True)
    resume = models.FileField('Резюме заявителя', upload_to=path_and_rename("award_files/resume/", 'resume'))
    video = models.TextField('Youtube ролик с видеопрезентацией проекта')
    presentation = models.FileField('Презентация проекта (форматы pptx/pdf)',
                                    upload_to=path_and_rename("award_files/presentations/", 'presentation'))
    jurys_nomination = models.ManyToManyField(NominationJury, verbose_name='Рекомендовать к номинации', blank=True)
    vote = models.ManyToManyField(Vote, verbose_name='Голос', blank=True)
    jury_approved = models.ManyToManyField(JuryApproved, verbose_name='Мнения жюри', blank=True)
    pub_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)
    to_edit_notification = models.TextField('Уведомление для участника', blank=True)
    for_jury_notification = models.TextField('Уведомление для жюри', blank=True)
    public_for_jury = models.BooleanField('На рассмотрение жюри', default=False)
    public = models.BooleanField('Опубликовать', default=False)

    def get_absolute_url(self):
        return reverse('request_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Заявка на премию'
        verbose_name_plural = 'Заявки на премию'


class Profile(models.Model):
    """Расширение пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User, verbose_name='Пользователь')
    jury = models.BooleanField('Статус жюри', default=False)
    partisipant = models.BooleanField('Статус участника', default=False)
    avatar = models.ImageField('Аватар (только для жюри)', null=True,
                               upload_to=path_and_rename("award_files/avatars/", 'jury'), blank=True)
    professional = models.CharField('Профессия (только для жюри)', max_length=200, null=True, blank=True)
    preview = RichTextUploadingField('Краткая информация(только для жюри)', null=True,
                               blank=True)
    interview = models.TextField('Ссылка на интервью (только для жюри)', null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class AwardPartner(models.Model):
    """Партнеры премии"""
    name = models.CharField('Название компании - партнера', max_length=300)
    url = models.URLField('Ссылка на сайт партнера', max_length=500)
    logo = models.ImageField('Логотип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class AwardNewParticipant(models.Model):
    """Заявка на участие в премии"""
    name = models.CharField('Имя', max_length=200)
    company = models.CharField('Компания', max_length=300)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новая заявка на участие'
        verbose_name_plural = 'Новые заявки на участие'
