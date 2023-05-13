from django.contrib import admin
from django.contrib.admin import register

from support.models import Message


@register(Message)
class PatientMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'condition', 'title', 'content', 'response']
    list_filter = ['condition']
