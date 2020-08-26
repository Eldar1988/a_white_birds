import os
from uuid import uuid4

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


def path_and_rename(path, prefix):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        # get filename
        filename = "{}.{}.{}".format(prefix, uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
        return wrapper


class InfoBlock(models.Model):
    """Блоки с информацией"""
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True)
    image = models.ImageField('Картинка', upload_to=path_and_rename("forum/", 'image'), help_text='https://undraw.co/')
    title = models.CharField('Заголовок блока', max_length=255)
    description = models.TextField('Описание блока')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок с описанием'
        verbose_name_plural = 'Блоки с описанием'


class ForumPartner(models.Model):
    """Партнеры форума"""
    name = models.CharField('Название компании', max_length=255)
    image = models.ImageField('Логотип', upload_to=path_and_rename("forum/", 'image'))
    url = models.URLField('Ссылка на сайт', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер форума'
        verbose_name_plural = 'Партнеры форума'


class ForumInfo(models.Model):
    """Общая информация о форуме"""
    title = models.CharField('Заголовок страницы форума', max_length=255)
    sub_title = models.CharField('Подзаголовок страницы форума', max_length=255)
    image = models.ImageField('Картинка', upload_to=path_and_rename("forum/", 'image'),
                              help_text='Не забудьте оптимизировать на сайте https://tinypng.com/', null=True)
    forum_description_title = models.CharField('Заголовок блока с описанием', max_length=255)
    forum_description = RichTextUploadingField('Описание форума')
    info_blocks = models.ManyToManyField(InfoBlock, verbose_name='Блоки с информацией',)
    forum_2020_text = RichTextUploadingField('Текст (заглушка для форума 202)', blank=True)
    forum_2020 = models.ImageField('Заглушка для форума 2020', upload_to=path_and_rename("forum/", 'image'), null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о форуме'
        verbose_name_plural = 'Информация о форуме'


class Facilitator(models.Model):
    """Фасилитаторы"""
    table = models.PositiveSmallIntegerField('Номер стола')
    name = models.CharField('Имя фасилитатора', max_length=255)
    company = models.CharField('Компания', max_length=255)
    company_logo = models.ImageField('Логотип компании', upload_to=path_and_rename("forum/", 'image'), null=True)
    avatar = models.ImageField('Фотография', upload_to=path_and_rename("forum/", 'image'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фасилитатор'
        verbose_name_plural = 'Фасилитаторы 2019'


class ForumParticipant(models.Model):
    """Участник форума"""
    table = models.PositiveSmallIntegerField('Номер стола')
    speaking_time = models.CharField('Время выступления', max_length=255)
    name = models.CharField('Имя участника', max_length=255)
    company = models.CharField('Компания', max_length=255)
    avatar = models.ImageField('Фотография', upload_to=path_and_rename("forum/", 'image'))
    presentation = models.FileField('Презентация', upload_to=path_and_rename("forum/", 'presentation'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры 2019'


class Facilitator2020(models.Model):
    """Фасилитаторы 2020 """
    table = models.PositiveSmallIntegerField('Номер стола')
    name = models.CharField('Имя фасилитатора', max_length=255)
    company = models.CharField('Компания', max_length=255)
    company_logo = models.ImageField('Логотип компании', upload_to=path_and_rename("forum/", 'image'), null=True)
    avatar = models.ImageField('Фотография', upload_to=path_and_rename("forum/", 'image'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фасилитатор'
        verbose_name_plural = 'Фасилитаторы 2020'


class ForumParticipant2020(models.Model):
    """Участник форума 2020"""
    table = models.PositiveSmallIntegerField('Номер стола')
    speaking_time = models.CharField('Время выступления', max_length=255)
    name = models.CharField('Имя участника', max_length=255)
    company = models.CharField('Компания', max_length=255)
    avatar = models.ImageField('Фотография', upload_to=path_and_rename("forum/", 'image'))
    presentation = models.FileField('Презентация', upload_to=path_and_rename("forum/", 'presentation'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры 2020'


class ForumNewParticipant(models.Model):
    """Заявка на участие в форуме"""
    name = models.CharField('Имя', max_length=200)
    company = models.CharField('Компания', max_length=300)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новая заявка на участие в форуме'
        verbose_name_plural = 'Новые заявки на участие в форуме'
