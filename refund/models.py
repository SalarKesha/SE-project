from django.db import models
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce

from doctor.models import Doctor
from visit.models import PatientVisit


class Refund(models.Model):
    patient_visit = models.ForeignKey(PatientVisit, related_name='refunds', on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField()

    def __str__(self):
        return f"{self.patient_visit.visit.doctor} {self.patient_visit.patient}"

    @classmethod
    def get_report(cls):
        total_refund = Sum('refunds__amount')
        users = Doctor.objects.all().annotate(
            refund_count=Count('refunds__id'),
            total=Coalesce(total_refund, 0)
        )
        return users

    @classmethod
    def get_total_balance(cls):
        refund_sum = Sum('refunds__amount')
        queryset = cls.get_report()
        total_refund = queryset.aggregate(total=Coalesce(refund_sum, 0))
        return total_refund['total']