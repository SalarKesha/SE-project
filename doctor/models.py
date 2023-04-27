from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from khayyam import *

# from account.models import CustomUser
from location.models import City


# from patient.models import PatientVisit


class Expertise(models.Model):
    title = models.CharField(max_length=42, blank=False, null=False)

    def f(self):
        return f"\'{self.title}\'"

    def __str__(self):
        return self.title


class Doctor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=11, unique=True, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctors')
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

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def get_first_visit(self):
        fv = self.visits.order_by('time').first()
        # if fv:
        #     return False
        # time = JalaliDate(fv)
        # return str(JalaliDate(2022, 11, 2))
        return fv

    def f(self):
        return f"\'{self.first_name} {self.last_name}\'"

    def __str__(self):
        return self.get_fullname()


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
        # now = datetime.now()
        # print(JalaliDatetime(now))
        date = JalaliDate(self.time).strftime('%A %D %B')
        time = JalaliDatetime(self.time).strftime(' %h:%v ')
        return str(date) + str(time)
        # return datetime.
        # return f"{self.time}"


class Request(models.Model):
    NEW = 1
    ACCEPT = 2
    REJECT = 3
    CONDITION = (
        (NEW, 'new'),
        (ACCEPT, 'accept'),
        (REJECT, 'reject')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_query_name='requests')
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=11)
    person_code = models.CharField(max_length=10)
    medical_code = models.CharField(max_length=12)
    expertise = models.ForeignKey(Expertise, on_delete=models.PROTECT, related_name='requests')
    office_number = models.CharField(max_length=11)
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='requests')
    address = models.TextField(null=True, blank=True)
    condition = models.PositiveSmallIntegerField(default=NEW, choices=CONDITION)
    photo = models.ImageField(blank=True, null=True, upload_to='requests/')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person_code} {self.medical_code} {self.get_condition_display()}"
