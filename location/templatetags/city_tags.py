from location.models import City
from django import template

register = template.Library()


@register.simple_tag
def get_cities():
    return City.objects.select_related('region').all()
