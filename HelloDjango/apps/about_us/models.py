from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from HelloDjango.settings import path_and_rename


class AboutUsInfo(models.Model):
    """Инофрмация о компании"""
    title = models.CharField('Заголовок страницы', max_length=255)
    text = RichTextUploadingField('Текст о компании')
    image = models.ImageField('Фото руководителя', upload_to=path_and_rename("about/", 'image'))
    photo_text = RichTextUploadingField('Текст под фото руководителя')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'


class ImageBlock(models.Model):
    """Блоки с картинками"""
    image = models.ImageField('Картинка', upload_to=path_and_rename("about/", 'image'))
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок с картинкой на странице о компании'
        verbose_name_plural = 'Блоки с картинкой на странице о компании'