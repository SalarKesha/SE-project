from django.core.paginator import Paginator
from django.db.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from doctor.models import Doctor


def test(request):
    return render(request, 'base/base.html')


class DoctorListView(ListView):
    queryset = Doctor.objects.all()
    context_object_name = 'doctors'
    template_name = 'doctor/search.html'
    paginate_by = 3


def search(request):
    if request.method == 'POST':
        doctor = request.POST.get('doctor')
        expertise = request.POST.get('expertise')
        city = request.POST.get('city')
        qs = Doctor.objects.filter(city__name=city).annotate(
            visit_count=Count('visits__id'),
        )
    else:
        qs = Doctor.objects.all().annotate(
            visit_count=Count('visits__id'),
        )
        city = False
    # paginator = Paginator(qs, 30)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, 'doctor/search.html', {'page_obj': qs, 'city': city})
