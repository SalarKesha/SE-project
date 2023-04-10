from django.contrib.auth.models import User
from django.db import models

from doctor.models import Visit, Doctor


class Patient(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=11, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"


class PatientVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name="PatientVisits")
    visit = models.ForeignKey(Visit, on_delete=models.PROTECT, related_name="PatientVisits")
    is_visited = models.BooleanField(default=False)

    # doctor = models.CharField(max_length=64)
    # doctor_id = models.CharField(max_length=10)
    # expertise = models.CharField(max_length=42)
    # time = models.DateTimeField()
    # office_number = models.CharField(max_length=11)
    # address = models.TextField()
    # amount = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.patient.user.username} {self.visit.id}"



