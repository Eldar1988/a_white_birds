# Generated by Django 3.0.6 on 2020-07-20 20:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20200715_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='edit_date',
        ),
        migrations.RemoveField(
            model_name='request',
            name='promocode',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='award_files/', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='request',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание проекта'),
        ),
        migrations.AddField(
            model_name='request',
            name='project_appoints',
            field=models.TextField(null=True, verbose_name='Преимущества проекта'),
        ),
        migrations.AddField(
            model_name='request',
            name='results',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Результаты, полученные после внедрения проекта'),
        ),
        migrations.AlterField(
            model_name='nominationjury',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название номинации к рекомендации'),
        ),
        migrations.AlterField(
            model_name='request',
            name='jurys_nomination',
            field=models.ManyToManyField(to='awards.NominationJury', verbose_name='Рекомендовать к номинации'),
        ),
        migrations.AlterField(
            model_name='request',
            name='resume',
            field=models.FileField(upload_to='award_files/', verbose_name='Резюме заявителя'),
        ),
        migrations.AlterField(
            model_name='request',
            name='video',
            field=models.URLField(verbose_name='Ссылка на Youtube ролик с видеопрезентацией проекта'),
        ),
    ]
