from django import forms
from django.core.exceptions import ValidationError

from account.validators import phone_number_validator


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=32, widget=forms.TextInput({'placeholder': 'نام'}), label='')
    last_name = forms.CharField(max_length=42, widget=forms.TextInput({'placeholder': 'نام خانوادگی'}), label='')
    phone_number = forms.CharField(widget=forms.NumberInput({'placeholder': 'شماره موبایل'}), validators=[phone_number_validator], label='')
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'رمز عبور'}), min_length=8, max_length=32, label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput({'placeholder': 'تکرار رمز عبور'}), label='')

    def clean_password_confirmation(self):
        password_confirmation = self.cleaned_data['password_confirmation']
        password = self.cleaned_data['password']
        if password_confirmation != password:
            raise ValidationError('تکرار رمز همخوانی ندارد!')
        return password_confirmation


class LoginForm(forms.Form):
    phone_number = forms.CharField(widget=forms.NumberInput({'placeholder': 'شماره موبایل'}), validators=[phone_number_validator], label='')
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'رمز عبور'}), min_length=8, max_length=32, label='')


class ForgetPasswordForm(forms.Form):
    phone_number = forms.CharField(widget=forms.NumberInput({'placeholder': 'شماره موبایل'}), validators=[phone_number_validator], label='')
