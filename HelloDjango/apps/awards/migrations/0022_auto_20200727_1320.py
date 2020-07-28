# Generated by Django 3.0.6 on 2020-07-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0021_auto_20200727_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='award_files/', verbose_name='Аватар (только для жюри)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interview',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на интервью (только для жюри)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preview',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Краткая информация - один абзац (только для жюри)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='professional',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Профессия (только для жюри)'),
        ),
        migrations.AlterField(
            model_name='request',
            name='video',
            field=models.TextField(verbose_name='Ссылка на Youtube ролик с видеопрезентацией проекта'),
        ),
    ]
