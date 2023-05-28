from django.urls import path, include

from support.views import message

urlpatterns = [
    path('<int:pk>/', message, name='message')
]
