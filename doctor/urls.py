from django.urls import path, include

from doctor.views import test, search, DoctorListView, profile, doctor_panel, doctor_expertise

urlpatterns = [
    path('test/', test),
    path('search/', search, name='search'),
    path('<int:pk>/', profile, name='doctor'),
    path('<int:pk>/panel/', doctor_panel, name='doctor_panel'),
    path('<int:upk>/panel/expertise/<int:epk>', doctor_expertise, name='doctor_expertise'),
]