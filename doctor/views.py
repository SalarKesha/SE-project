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
        name = request.POST.get('name')
        expertise = request.POST.get('expertise')
        city = request.POST.get('city')
        if name and expertise and city:
            qs = Doctor.objects.filter(
                Q(first_name__in=name.split()) | Q(last_name__in=name.split()),
                expertise__title=expertise,
                city__name=city
            )
            # city = False
            # expertise = False
            # name = False
        elif expertise and city:
            qs = Doctor.objects.filter(expertise__title=expertise, city__name=city)

        elif expertise and name:
            qs = Doctor.objects.filter(
                Q(first_name__in=name.split()) | Q(last_name__in=name.split()),
                expertise__title=expertise
            )
        elif name and city:
            qs = Doctor.objects.filter(
                Q(first_name__in=name.split()) | Q(last_name__in=name.split()),
                city__name=city
            )
        elif name:
            qs = Doctor.objects.filter(Q(first_name__in=name.split()) | Q(last_name__in=name.split()))

        elif expertise:
            qs = Doctor.objects.filter(expertise__title=expertise)
        elif city:
            qs = Doctor.objects.filter(city__name=city)
        else:
            qs = Doctor.objects.all()

        qs = qs.annotate(
            visit_count=Count('visits__id'),
        ).distinct()
        paginator = Paginator(qs, 30)
        page_number = request.POST.get('page')
        page_obj = paginator.get_page(page_number)

    else:
        qs = Doctor.objects.all()
        city = False
        expertise = False
        name = False
        qs = qs.annotate(
            visit_count=Count('visits__id'),
        ).distinct()
        paginator = Paginator(qs, 30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request, 'doctor/search.html', {'page_obj': page_obj, 'name': name, 'expertise': expertise, 'city': city})
