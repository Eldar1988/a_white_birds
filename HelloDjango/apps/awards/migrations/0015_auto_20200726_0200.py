# Generated by Django 3.0.6 on 2020-07-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0014_auto_20200725_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juryapproved',
            name='award_request',
        ),
        migrations.AddField(
            model_name='request',
            name='jury_approved',
            field=models.ManyToManyField(blank=True, to='awards.JuryApproved', verbose_name='Мнения жюри'),
        ),
    ]
