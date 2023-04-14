from django import template

from doctor.models import Doctor

register = template.Library()


@register.simple_tag
def get_doctors():
    return Doctor.objects.all().distinct('first_name', 'last_name')
