from django.urls import path, include
from patient.views import panel
urlpatterns = [
    path('<int:pk>/', panel, name='patient_panel'),
]
