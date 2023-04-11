from django.contrib import admin
from django.contrib.admin import register

from visit.models import PatientVisit


# Register your models here.


@register(PatientVisit)
class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'visit', 'is_visited']
    search_fields = ['id', 'patient__phone_number', 'visit__id', 'visit__doctor_id']
    list_filter = ['is_visited']
