from django.contrib import admin

from django.contrib import admin
from .models import HhRequest, Profile, Sphere, Experience, WorkRequest


@admin.register(HhRequest)
class HhRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile', 'sphere', 'experience', 'work_request', 'pub_date')
    readonly_fields = ('user', 'profile', 'sphere', 'experience', 'work_request', 'pub_date', 'email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Sphere)
class SphereAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(WorkRequest)
class WorkRequestAdmin(admin.ModelAdmin):
    list_display = ('name',)


