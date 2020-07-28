# Generated by Django 3.0.6 on 2020-07-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('logo', models.ImageField(upload_to='images/', verbose_name='Логотип компании')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('address', models.TextField(verbose_name='Адрес компании')),
                ('copyright', models.TextField(help_text='Будет расположен в футере', verbose_name='Копирайт')),
            ],
        ),
    ]
