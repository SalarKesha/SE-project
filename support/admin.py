from django.contrib import admin
from django.contrib.admin import register

from support.models import DoctorMessage, PatientMessage


@register(DoctorMessage)
class DoctorMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'condition', 'title', 'content', 'response']
    list_filter = ['condition']


@register(PatientMessage)
class PatientMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'condition', 'title', 'content', 'response']
    list_filter = ['condition']
