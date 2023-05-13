from django.conf import settings
from django.db import models

from doctor.models import Doctor
from patient.models import Patient


class Message(models.Model):
    NEW = 1
    SEEN_ONLY = 2
    ANSWERED = 3
    CONDITION = (
        (NEW, 'new'),
        (SEEN_ONLY, 'seen_only'),
        (ANSWERED, 'answered')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    condition = models.PositiveSmallIntegerField(default=NEW, choices=CONDITION)
    created_time = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} {self.content}"
