# Generated by Django 3.0.6 on 2020-09-15 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_forumparticipant_special_quest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumparticipant',
            name='special_quest',
        ),
        migrations.AddField(
            model_name='facilitator',
            name='special_quest',
            field=models.BooleanField(default=False, verbose_name='Специальный гость'),
        ),
        migrations.AddField(
            model_name='facilitator2020',
            name='special_quest',
            field=models.BooleanField(default=False, verbose_name='Специальный гость'),
        ),
    ]
