from django.contrib import admin
from .models import ServiceInfo, SubService, Service, ServiceContact, Profile, Sphere, Experience, SelfRequest, \
    ServiceContactResume

admin.site.register(Profile)
admin.site.register(Sphere)
admin.site.register(Experience)
admin.site.register(SelfRequest)


@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'form', 'form_resume')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ServiceContact)
class ServiceContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'comment', 'service')
    list_filter = ('service',)


@admin.register(ServiceContactResume)
class ServiceContactResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'profile', 'sphere', 'experience', 'self_request')
    readonly_fields = ('name', 'phone', 'email', 'profile', 'sphere', 'experience', 'self_request')
    list_filter = ('profile', 'sphere', 'experience', 'self_request')