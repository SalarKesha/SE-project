from django.urls import path, include

from doctor.views import test, search, DoctorListView, profile

urlpatterns = [
    path('test/', test),
    path('search/', search, name='search'),
    path('<int:pk>/', profile, name='doctor'),
]