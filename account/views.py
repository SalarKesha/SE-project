from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from account.models import CustomUser


# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        try:
            CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=phone_number,
                password=password,
            )
            messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
            return redirect('login')
        except:
            messages.error(request, 'کاربری با این شماره موبایل ثبت نام کرده است', 'error')
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
        is_login = login(request, user)
        if user:
            messages.success(request, 'با موفقیت وارد شدید', 'success')
        else:
            messages.error(request, 'شماره موبایل و یا رمز عبور صحیح نمی باشد!', 'error')
        return redirect('login')
    else:
        return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
