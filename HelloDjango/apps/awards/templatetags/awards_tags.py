from django import template
from apps.awards.models import Request, Nomination, AwardPartner


register = template.Library()


@register.simple_tag()
def get_award_requests():
    award_requests = Request.objects.filter(public=True)
    return award_requests


@register.simple_tag()
def get_nominations():
    nomination = Nomination.objects.all()
    return nomination


@register.simple_tag()
def get_partners():
    partners = AwardPartner.objects.all()
    return partners
