from django import template
from apps.main.models import MainInfo


register = template.Library()


@register.simple_tag()
def get_info():
    main = MainInfo.objects.last()
    return main
