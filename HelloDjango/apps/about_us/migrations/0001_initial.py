# Generated by Django 3.0.6 on 2020-09-02 11:40

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок страницы')),
                ('forum_2020_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст о компании')),
                ('image', models.ImageField(upload_to=None, verbose_name='Фото руководителя')),
                ('photo_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст о компании')),
            ],
            options={
                'verbose_name': 'Информация о компании',
                'verbose_name_plural': 'Информация о компании',
            },
        ),
        migrations.CreateModel(
            name='ImageBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None, verbose_name='Картинка')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
        ),
    ]