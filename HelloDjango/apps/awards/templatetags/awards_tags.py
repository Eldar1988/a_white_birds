from django import template
from apps.awards.models import Request, Nomination

register = template.Library()


@register.simple_tag()
def get_award_requests():
    award_requests = Request.objects.filter(public=True)
    return award_requests


@register.simple_tag()
def get_nominations():
    nomination = Nomination.objects.all()
    return nomination
