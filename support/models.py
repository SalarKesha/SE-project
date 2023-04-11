from django.db import models

from doctor.models import Doctor
from patient.models import Patient


# class Message(models.Model):
#     ADMIN = 1
#     PATIENT = 2
#     DOCTOR = 3
#     HUMAN_TYPE = (
#         (ADMIN, "admin"),
#         (PATIENT, "patient"),
#         (DOCTOR, "doctor")
#     )
#     NEW = 1
#     READ = 2
#     CONDITION = (
#         (NEW, 'new'),
#         (READ, 'read')
#     )
#     sender_type = models.PositiveSmallIntegerField(default=ADMIN, choices=HUMAN_TYPE)
#     receiver_type = models.PositiveSmallIntegerField(default=ADMIN, choices=HUMAN_TYPE)
#     sender = models.CharField(max_length=10, null=False, blank=False)
#     receiver = models.CharField(max_length=10, null=False, blank=False)
#     title = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     condition = models.PositiveSmallIntegerField(default=NEW, choices=CONDITION)
#     created_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.sender} {self.receiver} {self.content}"


class DoctorMessage(models.Model):
    NEW = 1
    SEEN_ONLY = 2
    ANSWERED = 3
    CONDITION = (
        (NEW, 'new'),
        (SEEN_ONLY, 'seen_only'),
        (ANSWERED, 'answered')
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='messages')
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    condition = models.PositiveSmallIntegerField(default=NEW, choices=CONDITION)
    created_time = models.DateTimeField(auto_now_add=True)
    response = models.TextField()

    def __str__(self):
        return f"{self.doctor} {self.content}"


class PatientMessage(models.Model):
    NEW = 1
    SEEN_ONLY = 2
    ANSWERED = 3
    CONDITION = (
        (NEW, 'new'),
        (SEEN_ONLY, 'seen_only'),
        (ANSWERED, 'answered')
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='messages')
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    condition = models.PositiveSmallIntegerField(default=NEW, choices=CONDITION)
    created_time = models.DateTimeField(auto_now_add=True)
    response = models.TextField()

    def __str__(self):
        return f"{self.patient} {self.content}"
