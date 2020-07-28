# Generated by Django 3.0.6 on 2020-07-25 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0013_auto_20200725_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juryapproved',
            name='nomination_jury',
        ),
        migrations.AddField(
            model_name='juryapproved',
            name='nomination_jury',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='awards.NominationJury', verbose_name='Рекомендация к номинации'),
        ),
    ]