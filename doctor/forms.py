from django import forms


class Register(forms.Form):
    name = forms.CharField(label='نام پزشک')
    expertise = forms.CharField(label='تلفن همراه', max_length=11)
    city = forms.CharField(label='رمز عبور')
