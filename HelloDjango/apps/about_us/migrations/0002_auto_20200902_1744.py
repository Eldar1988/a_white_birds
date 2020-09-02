# Generated by Django 3.0.6 on 2020-09-02 11:44

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageblock',
            options={'verbose_name': 'Блок с картинкой на странице о компании', 'verbose_name_plural': 'Блоки с картинкой на странице о компании'},
        ),
        migrations.RenameField(
            model_name='aboutusinfo',
            old_name='forum_2020_text',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='aboutusinfo',
            name='photo_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст под фото руководителя'),
        ),
    ]