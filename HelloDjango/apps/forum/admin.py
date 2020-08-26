from django.contrib import admin

from .models import InfoBlock, ForumInfo, Facilitator, ForumParticipant, ForumPartner, ForumNewParticipant, \
    ForumParticipant2020, Facilitator2020

admin.site.register(ForumInfo)
admin.site.register(InfoBlock)
admin.site.register(Facilitator)
admin.site.register(Facilitator2020)
admin.site.register(ForumParticipant)
admin.site.register(ForumParticipant2020)
admin.site.register(ForumPartner)
admin.site.register(ForumNewParticipant)

