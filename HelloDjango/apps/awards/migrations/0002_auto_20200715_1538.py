# Generated by Django 3.0.6 on 2020-07-15 09:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nomination',
            options={'verbose_name': 'Номинация', 'verbose_name_plural': 'Номинации'},
        ),
        migrations.AlterModelOptions(
            name='nominationjury',
            options={'verbose_name': 'Номинация от жюри', 'verbose_name_plural': 'Номинации от жюри'},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jury', models.BooleanField(default=False, verbose_name='Статус жюри')),
                ('partisipant', models.BooleanField(default=False, verbose_name='Статус участника')),
                ('user', models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
