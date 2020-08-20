# Generated by Django 3.0.6 on 2020-08-19 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumprogram',
            name='Participant',
        ),
        migrations.AddField(
            model_name='forumprogram',
            name='Participant',
            field=models.ManyToManyField(to='forum.ForumParticipant', verbose_name='Участники'),
        ),
        migrations.RemoveField(
            model_name='forumprogram',
            name='facilitator',
        ),
        migrations.AddField(
            model_name='forumprogram',
            name='facilitator',
            field=models.ManyToManyField(to='forum.Facilitator', verbose_name='Фасилитаторы'),
        ),
    ]