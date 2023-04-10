from django.contrib.auth.models import User
from django.db import models

from location.models import City


# from patient.models import PatientVisit


class Expertise(models.Model):
    title = models.CharField(max_length=42, blank=False, null=False)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=11, unique=True, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    person_code = models.CharField(max_length=10)
    medical_code = models.CharField(max_length=5)
    expertise = models.ForeignKey(Expertise, on_delete=models.PROTECT, related_name='doctors')
    office_number = models.CharField(max_length=11)
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='doctors')
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, null=True, upload_to='doctors/')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="visits")
    time = models.DateTimeField()
    amount = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_taken = models.BooleanField(default=False)
    # city = models.CharField(max_length=32)
    # expertise = models.CharField(max_length=42)
    # office_number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.time}"


class Request(models.Model):
    NEW = 1
    ACCEPT = 2
    REJECT = 3
    CONDITION = (
        (NEW, 'new'),
        (ACCEPT, 'accept'),
        (REJECT, 'reject')
    )
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=11)
    person_code = models.CharField(max_length=10)
    medical_code = models.CharField(max_length=12)
    expertise = models.ForeignKey(Expertise, on_delete=models.PROTECT, related_name='requests')
    office_number = models.CharField(max_length=11)
    email = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='requests')
    address = models.TextField(null=True, blank=True)
    condition = models.PositiveSmallIntegerField(default=NEW, choices=CONDITION)
    photo = models.ImageField(blank=True, null=True, upload_to='requests/')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person_code} {self.medical_code} {self.get_condition_display()}"



