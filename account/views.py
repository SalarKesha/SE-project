from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from account.forms import RegisterForm, LoginForm, ForgetPasswordForm
from account.local_utils import send_code
from account.models import CustomUser
from patient.models import Patient


# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('fname')
#         last_name = request.POST.get('lname')
#         phone_number = request.POST.get('phone_number')
#         password = request.POST.get('password')
#         try:
#             with transaction.atomic():
#                 user = CustomUser.objects.create_user(
#                     first_name=first_name,
#                     last_name=last_name,
#                     username=phone_number,
#                     password=password,
#                 )
#                 Patient.objects.create(
#                     first_name=first_name,
#                     last_name=last_name,
#                     user=user,
#                     phone_number=phone_number
#                 )
#             messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
#             return redirect('login')
#         except:
#             messages.error(request, 'اطلاعات وارد شده صحیح نمی باشد!', 'error')
#             return redirect('signup')
#         # user = authenticate(request, username=phone_number, password=password)
#         # login(request, user)
#         # if user:
#         #     messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
#         #     return redirect('login')
#         # else:
#         #     messages.error(request, 'اطلاعات را به درستی وارد کنید', 'error')
#         #     return redirect('signup')
#     else:
#         return render(request, 'auth/signup.html')


# def login_user(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         password = request.POST.get('password')
#         user = authenticate(request, username=phone_number, password=password)
#         if user:
#             role = CustomUser.objects.get(username=phone_number).role
#             login(request, user)
#             messages.success(request, 'با موفقیت وارد شدید', 'success')
#             if role == 1:
#                 return redirect('patient_panel', request.user.id)
#             elif role == 2:
#                 return redirect('doctor_panel', request.user.id)
#             else:
#                 raise Http404
#
#         messages.error(request, 'شماره موبایل و یا رمز عبور صحیح نمی باشد!', 'error')
#     return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    messages.error(request, 'از حساب خود خارج شدید', 'error')
    return redirect('home')


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUser.objects.filter(username=cd['phone_number']).first()
            if user:
                messages.error(request, 'شخصی با این شماره قبلا ثبت نام کرده است!', 'error')
                return redirect('signup')
            try:
                with transaction.atomic():
                    user = CustomUser.objects.create_user(
                        first_name=cd['first_name'],
                        last_name=cd['last_name'],
                        username=cd['phone_number'],
                        password=cd['password'],
                    )
                    Patient.objects.create(
                        first_name=cd['first_name'],
                        last_name=cd['last_name'],
                        user=user,
                        phone_number=cd['phone_number']
                    )
                messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
                login(request, user)
                return redirect('home')
                # return redirect('patient_panel', user.id)
            except:
                messages.error(request, 'اطلاعات را به درستی وارد کنید', 'error')
    else:
        form = RegisterForm()
    return render(request, 'auth/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['phone_number'], password=cd['password'])
            if user:
                role = CustomUser.objects.get(username=cd['phone_number']).role
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید', 'success')
                if role == 1:
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    return redirect('patient_panel', user.id)
                elif role == 2:
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    return redirect('doctor_panel', user.id)
                else:
                    raise Http404
            else:
                messages.error(request, 'اطلاعات وارد شده صحیح نمی باشد', 'error')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def forget_password(request):
    if request.method == "POST":
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone_number = cd['phone_number']
            new_password = CustomUser.objects.make_random_password(length=8)
            try:
                with transaction.atomic():
                    user = CustomUser.objects.get(username=phone_number)
                    user.set_password(new_password)
                    user.save()
                    send_code(phone_number, new_password)
                    messages.success(request, 'رمز عبور جدید به شماره موبایل پیامک شد', 'success')
            except CustomUser.DoesNotExist:
                messages.error(request, 'شماره موبایل در سامانه ثبت نشده است!', 'error')
                return redirect('forgot_password')
            return redirect('login')
    else:
        form = ForgetPasswordForm
    return render(request, 'auth/forget_password.html', {'form': form})
