from django.contrib import admin
from django.contrib.admin import register

from patient.models import Patient


@register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number', 'created_time', 'modified_time']
    search_fields = ['id', 'first_name', 'last_name', 'phone_number']



