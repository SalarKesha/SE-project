from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from account.models import CustomUser
from patient.models import Patient


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        try:
            with transaction.atomic():
                user = CustomUser.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=phone_number,
                    password=password,
                )
                Patient.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    user=user,
                    phone_number=phone_number
                )
            messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
            return redirect('login')
        except:
            messages.error(request, 'اطلاعات وارد شده صحیح نمی باشد!', 'error')
            return redirect('signup')
        # user = authenticate(request, username=phone_number, password=password)
        # login(request, user)
        # if user:
        #     messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
        #     return redirect('login')
        # else:
        #     messages.error(request, 'اطلاعات را به درستی وارد کنید', 'error')
        #     return redirect('signup')
    else:
        return render(request, 'auth/signup.html')


def login_user(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = authenticate(request, username=phone_number, password=password)
        if user:
            role = CustomUser.objects.get(username=phone_number).role
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید', 'success')
            if role == 1:
                return redirect('patient_panel', request.user.id)
            elif role == 2:
                return redirect('doctor_panel', request.user.id)
            else:
                raise Http404

        messages.error(request, 'شماره موبایل و یا رمز عبور صحیح نمی باشد!', 'error')
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'از حساب خود خارج شدید', 'success')
    return redirect('home')
