# Generated by Django 3.0.8 on 2020-07-26 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0018_vote_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name': 'Голос', 'verbose_name_plural': 'Голоса'},
        ),
    ]
