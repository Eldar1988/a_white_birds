# Generated by Django 3.0.6 on 2020-07-25 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0008_request_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='public_for_jury',
            field=models.BooleanField(default=False, verbose_name='На рассмотрение жюри'),
        ),
    ]
