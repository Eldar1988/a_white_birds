# Generated by Django 3.0.6 on 2020-07-25 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0009_request_public_for_jury'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='for_jury_notification',
            field=models.TextField(blank=True, verbose_name='Уведомление для жюри'),
        ),
    ]