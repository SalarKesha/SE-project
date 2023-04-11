from django.contrib import admin
from django.contrib.admin import register

from refund.models import Refund


# Register your models here.
@register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient_visit', 'time', 'amount']
    search_fields = ['patient_visit__doctor_id', 'visit__id']
