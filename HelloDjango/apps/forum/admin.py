from django.contrib import admin

from .models import InfoBlock, ForumInfo, Facilitator, ForumParticipant, ForumPartner, ForumNewParticipant

admin.site.register(ForumInfo)
admin.site.register(InfoBlock)
admin.site.register(Facilitator)
admin.site.register(ForumParticipant)
admin.site.register(ForumPartner)
admin.site.register(ForumNewParticipant)

