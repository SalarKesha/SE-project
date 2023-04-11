from django.db import models

from doctor.models import Doctor, Visit
from patient.models import Patient
from transaction.models import Transaction


# Create your models here.
class PatientVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name="PatientVisits")
    visit = models.ForeignKey(Visit, on_delete=models.PROTECT, related_name="PatientVisit")
    is_visited = models.BooleanField(default=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT, related_name='patient_visit')

    # doctor = models.CharField(max_length=64)
    # doctor_id = models.CharField(max_length=10)
    # expertise = models.CharField(max_length=42)
    # time = models.DateTimeField()
    # office_number = models.CharField(max_length=11)
    # address = models.TextField()
    # amount = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.patient.user.username} {self.visit.id}"
