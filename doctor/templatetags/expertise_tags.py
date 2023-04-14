from django import template

from doctor.models import Expertise

register = template.Library()


@register.simple_tag
def get_expertises():
    return Expertise.objects.all()
