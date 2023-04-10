from django.urls import path, include

from doctor.views import test

urlpatterns = [
    path('test/', test),
]