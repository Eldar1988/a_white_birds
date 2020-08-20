# Generated by Django 3.0.6 on 2020-08-19 05:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200819_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='foruminfo',
            name='image',
            field=models.ImageField(help_text='Не забудьте оптимизировать на сайте https://tinypng.com/', null=True, upload_to=None, verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='foruminfo',
            name='forum_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание форума'),
        ),
        migrations.DeleteModel(
            name='ForumProgram',
        ),
    ]
