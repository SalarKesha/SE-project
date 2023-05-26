from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce

from doctor.models import Doctor, Visit
from patient.models import Patient


class Transaction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='transactions')
    visit = models.ForeignKey(Visit, on_delete=models.PROTECT, related_name='transactions')
    amount = models.BigIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.visit} {self.amount}"

    @classmethod
    def get_report(cls):
        transaction_sum = Sum('transactions__amount')
        users = Doctor.objects.all().annotate(
            refund_count=Count('transactions__id'),
            total=Coalesce(transaction_sum, 0)
        )
        return users

    @classmethod
    def get_total_balance(cls):
        transaction_sum = Sum('transactions__amount')
        queryset = cls.get_report()
        total_transaction = queryset.aggregate(total=Coalesce(transaction_sum, 0))
        return total_transaction['total']


class DoctorBalance(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name='balances')
    balance = models.BigIntegerField()

    def __str__(self):
        return f"{self.doctor} {self.balance}"

    @classmethod
    def record_doctor_balance(cls, doctor):
        positive_transactions = Sum('amount')
        negative_transactions = Sum('amount')
        visits = doctor.visits.filter(is_taken=True)
        doctor_visits = Transaction.objects.filter(visit__in=visits).aggregate(
            balance=Coalesce(positive_transactions, 0)
        )
        # doctor_refunds = doctor.visits.patient_visit.refunds.all().aggregate(
        #     balance=Coalesce(negative_transactions, 0)
        # )
        # doctor_balance = doctor_visits['balance'] - doctor_refunds['balance']
        # return doctor_balance
        return doctor_visits['balance']
