from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    PATIENT = 1
    DOCTOR = 2
    ADMIN = 3
    ROLES = [
        (PATIENT, 'patient'),
        (DOCTOR, 'doctor'),
        (ADMIN, 'admin')
    ]
    role = models.PositiveSmallIntegerField(default=PATIENT, choices=ROLES)
