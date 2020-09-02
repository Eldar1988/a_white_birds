# Generated by Django 3.0.6 on 2020-09-02 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='form',
        ),
        migrations.RemoveField(
            model_name='service',
            name='form_resume',
        ),
        migrations.AddField(
            model_name='subservice',
            name='form',
            field=models.BooleanField(default=False, verbose_name='Форма заявки'),
        ),
        migrations.AddField(
            model_name='subservice',
            name='form_resume',
            field=models.BooleanField(default=False, verbose_name='Форма с резюме'),
        ),
    ]