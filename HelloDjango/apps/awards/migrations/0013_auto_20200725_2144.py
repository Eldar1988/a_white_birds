# Generated by Django 3.0.6 on 2020-07-25 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0012_auto_20200725_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juryapproved',
            name='award_request',
        ),
        migrations.AddField(
            model_name='juryapproved',
            name='award_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='awards.Request', verbose_name='Заявка'),
        ),
    ]
