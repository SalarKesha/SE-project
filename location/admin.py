from django.contrib import admin
from django.contrib.admin import register

from location.models import City, Region


@register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']
    search_fields = ['name']


@register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
