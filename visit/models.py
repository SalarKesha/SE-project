from django.db import models

from doctor.models import Doctor, Visit
from patient.models import Patient
from transaction.models import Transaction


# Create your models here.
class PatientVisit(models.Model):
    NOT_VISITED = 1
    VISITED = 2
    REFUNDED = 3
    CONDITION = (
        (NOT_VISITED, 'not_visited'),
        (VISITED, 'visited'),
        (REFUNDED, 'refunded')
    )
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name="patient_visits")
    visit = models.ForeignKey(Visit, on_delete=models.PROTECT, related_name="patient_visit")
    condition = models.SmallIntegerField(choices=CONDITION, default=NOT_VISITED)
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT, related_name='patient_visit')

    # doctor = models.CharField(max_length=64)
    # doctor_id = models.CharField(max_length=10)
    # expertise = models.CharField(max_length=42)
    # time = models.DateTimeField()
    # office_number = models.CharField(max_length=11)
    # address = models.TextField()
    # amount = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.patient} {self.visit.id}"
