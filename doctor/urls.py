from django.urls import path, include

from doctor.views import test, search, DoctorListView

urlpatterns = [
    path('test/', test),
    path('search/', search, name='search'),
]