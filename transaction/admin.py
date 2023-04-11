from django.contrib import admin
from django.contrib.admin import register
from transaction.models import Transaction, DoctorBalance


@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'visit', 'amount', 'time']
    search_fields = ['patient__id', 'visit__id']


@register(DoctorBalance)
class DoctorBalanceAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'balance']
    search_fields = ['doctor__id', 'doctor__phone_number']
