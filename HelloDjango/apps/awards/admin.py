from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import \
    AwardInfo, \
    AwardsIconBlock, \
    Nomination, \
    NominationJury, \
    Vote, \
    Request, JuryApproved, Profile


@admin.register(AwardInfo)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('award_title',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('ip',)


@admin.register(AwardsIconBlock)
class AwardsIconBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    list_editable = ('icon',)
    save_as = True


@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    save_as = True


@admin.register(NominationJury)
class NominationJuryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    save_as = True


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_name', 'company', 'email', 'phone', 'nomination', 'public', 'public_for_jury', 'pub_date')
    list_filter = ('nomination', 'public_for_jury', 'public')
    list_editable = ('public', 'public_for_jury')
    search_fields = ('name',)
    save_as = True

    class TabularItemInline(admin.TabularInline):
        classes = ('grp-collapse grp-open',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'jury', 'partisipant')
    list_filter = ('jury', 'partisipant')
    save_as = True


@admin.register(JuryApproved)
class JuryApprovedAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'approved', 'recommendation', 'vote')
    list_editable = ('approved',)
    search_fields = ('project', 'name', 'recommendation')
    list_filter = ('name', 'approved', 'project')


admin.site.site_title = 'White Birds'
admin.site.site_header = 'White Birds - администрирование'