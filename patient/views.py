from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from account.models import CustomUser
from patient.models import Patient
from visit.models import PatientVisit


@login_required(login_url='/login')
def panel(request, pk):
    user = CustomUser.objects.filter(id=pk).first()
    if user != request.user:
        raise Http404
    try:
        patient = Patient.objects.get(user_id=pk)
    except Patient.DoesNotExist:
        raise Http404
    visits = patient.patient_visits.all()
    return render(request, 'patient/panel.html', {'patient': patient, 'visits': visits})
