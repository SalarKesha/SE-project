from django.contrib import admin
from django.contrib.admin import register

from patient.models import Patient, PatientVisit


@register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number', 'created_time', 'modified_time']
    search_fields = ['id', 'first_name', 'last_name', 'phone_number']


@register(PatientVisit)
class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'visit', 'is_visited']
    search_fields = ['id', 'patient__phone_number', 'visit__id', 'visit__doctor_id']
    list_filter = ['is_visited']
