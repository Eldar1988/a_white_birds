from django import template
from ..forms import WorkRequestForm


register = template.Library()


@register.simple_tag()
def get_hh_form():
    hh_request_form = WorkRequestForm
    return hh_request_form
