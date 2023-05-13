from django.urls import path, include

from support.views import message

urlpatterns = [
    path('support/<int:pk>', message, name='message')
]
