# Generated by Django 3.0.6 on 2020-07-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0015_auto_20200726_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='juryapproved',
            name='project',
            field=models.CharField(blank=True, max_length=200, verbose_name='Проект'),
        ),
    ]
