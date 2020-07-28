# Generated by Django 3.0.8 on 2020-07-26 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0017_auto_20200726_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь на сайте'),
        ),
    ]