# Generated by Django 3.0.6 on 2020-07-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0007_auto_20200723_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ваша фотография'),
        ),
    ]
