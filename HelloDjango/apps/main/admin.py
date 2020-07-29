from django.contrib import admin
# from django.utils.safestring import mark_safe

from .models import MainInfo, TelegramBot


@admin.register(MainInfo)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ('number', 'purpose', 'url', 'chat_id')
