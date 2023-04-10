from django.contrib import admin
from django.contrib.admin import register

from support.models import Message


@register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender_type', 'receiver_type', 'sender', 'receiver', 'condition', 'title', 'content']
    list_filter = ['sender_type', 'receiver_type', 'condition']
