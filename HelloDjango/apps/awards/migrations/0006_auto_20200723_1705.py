# Generated by Django 3.0.6 on 2020-07-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_auto_20200723_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='presentation',
            field=models.FileField(upload_to='award_files/', verbose_name='Презентация проекта (форматы pptx/pdf)'),
        ),
    ]
