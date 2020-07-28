from django.contrib import admin
# from django.utils.safestring import mark_safe

from .models import MainInfo


@admin.register(MainInfo)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name',)

