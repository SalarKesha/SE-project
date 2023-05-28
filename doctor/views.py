from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import *
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from account.models import CustomUser
from doctor.models import Doctor, Request, Expertise, Visit
from doctor.utils import fix_datetime, set_visit
# from doctor.utils import validate
from location.models import City
from patient.models import Patient
from transaction.models import DoctorBalance, Transaction
from visit.models import PatientVisit


def test(request):
    password = CustomUser.objects.make_random_password(length=8)
    return HttpResponse(password)


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
    return render(request, 'doctor/search.html',
                  {'page_obj': page_obj, 'name': name, 'expertise': expertise, 'city': city})


def profile(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        raise Http404
    visits = doctor.visits.filter(is_taken=False).order_by('time')
    return render(request, 'doctor/profile.html', {'doctor': doctor, 'visits': visits})


@login_required(login_url='/login/')
def doctor_visit(request, pk):
    try:
        visit = Visit.objects.get(pk=pk)
        if visit.is_taken:
            return HttpResponse('این نوبت توسط شخص دیگری گرفته شده است!')
    except Visit.DoesNotExist:
        raise Http404
    if request.method == "POST":
        patient = Patient.objects.get(user_id=request.user.id)
        visit_id = request.POST.get('id')
        try:
            visit = Visit.objects.get(pk=visit_id)
            if visit.is_taken:
                raise Http404
        except Visit.DoesNotExist:
            raise Http404
        transaction = Transaction.objects.create(
            patient=patient,
            visit=visit,
            amount=visit.amount
        )
        patient_visit = PatientVisit.objects.create(
            visit=visit,
            patient=patient,
            transaction=transaction
        )
        visit.is_taken = True
        visit.save()
        return redirect('patient_panel', request.user.id)
    return render(request, 'doctor/doctor_visit.html', {'visit': visit})


@login_required(login_url='/login/')
# @user_passes_test(validate(request=request), login_url='/login/',)
def doctor_panel(request, pk):
    user = CustomUser.objects.filter(id=pk).first()
    if user != request.user:
        raise Http404
    doctors = user.doctors.all()
    return render(request, 'doctor/doctor_panel.html', {'doctors': doctors})


@login_required(login_url='/login/')
def doctor_expertise(request, upk, epk):
    user = CustomUser.objects.filter(id=upk).first()
    if user != request.user:
        raise Http404
    doctor = Doctor.objects.filter(user_id=upk, expertise_id=epk).first()
    if request.method == 'POST':
        set_visit(request, doctor)
    visits = doctor.visits.all().order_by('time')
    # try:
    balance = DoctorBalance.record_doctor_balance(doctor=doctor)
    # except:
    #     balance = False
    return render(request, 'doctor/doctor_expertise.html', {'doctor': doctor, 'visits': visits, 'balance': balance})


@login_required(login_url='/login/')
def doctor_request(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            medical_code = request.POST.get('code')
            person_code = request.POST.get('pid')
            phone_number = request.POST.get('number')
            office_number = request.POST.get('onumber')
            address = request.POST.get('address')
            email = request.POST.get('email')
            photo = request.POST.get('photo')
            user = CustomUser.objects.filter(username=phone_number).first()
            city = City.objects.get(name=request.POST.get('city'))
            expertise = Expertise.objects.get(title=request.POST.get('expertise'))
            Request.objects.create(
                user=user, first_name=first_name, last_name=last_name, medical_code=medical_code,
                person_code=person_code,
                city=city, expertise=expertise, phone_number=phone_number, office_number=office_number, address=address,
                email=email, photo=photo
            )
            messages.success(request, 'درخواست با موفقیت ثبت شد', 'success')
            # return redirect('home')
        except:
            # messages.error(request, 'اطلاعات را به درستی وارد کنید', 'error')
            messages.error(request, 'اطلاعات را به درستی وارد کنید', 'error')

    return render(request, 'doctor/request.html',
                  {'phone_number': request.user.username, 'fname': request.user.first_name,
                   'lname': request.user.last_name})
