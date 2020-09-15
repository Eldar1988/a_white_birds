# Generated by Django 3.0.6 on 2020-09-15 01:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20200826_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumparticipant',
            name='company',
        ),
        migrations.AddField(
            model_name='facilitator',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Био'),
        ),
        migrations.AddField(
            model_name='forumparticipant',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Био'),
        ),
        migrations.AddField(
            model_name='forumparticipant',
            name='company_logo',
            field=models.ImageField(null=True, upload_to=None, verbose_name='Логотип компании'),
        ),
    ]
