from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.models import User

from account.models import CustomUser
from doctor.models import Doctor, Expertise, Request, Visit


@admin.action(description='Accept')
def accept(modeladmin, request, queryset):
    queryset.update(condition=2)
    for req in queryset:
        # password = CustomUser.objects.make_random_password(length=8)
        # user = CustomUser.objects.get(username=user.password).update(
        #     password=password,
        #     role=2
        # )
        # send_notif(user.username, user.password)
        user = CustomUser.objects.get(username=req.phone_number)
        doctor = Doctor.objects.create(
            user=user,
            first_name=req.first_name,
            last_name=req.last_name,
            person_code=req.person_code,
            medical_code=req.medical_code,
            expertise=req.expertise,
            phone_number=req.phone_number,
            office_number=req.office_number,
            email=req.email,
            city=req.city,
            address=req.address,
        )
        if req.photo:
            doctor.photo = req.photo
        doctor.save()
        user.role = 2
        user.save()


@admin.action(description='Reject')
def reject(modeladmin, request, queryset):
    queryset.update(condition=3)


@register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'person_code', 'medical_code', 'expertise', 'phone_number',
                    'office_number', 'email', 'city', 'address', 'is_active', 'created_time', 'modified_time', 'photo']
    list_filter = ['is_active']
    search_fields = ['id', 'first_name', 'last_name', 'person_code', 'medical_code', 'phone_number', 'office_number']


@register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'person_code', 'medical_code', 'expertise', 'phone_number',
                    'office_number', 'email', 'city', 'address', 'condition', 'created_time', 'photo']
    search_fields = ['id', 'person_code', 'medical_code', 'phone_number']
    list_filter = ['condition']
    actions = [accept, reject]


@register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'time', 'amount', 'is_active', 'is_taken']
    # list_display = ['id', 'doctor', 'doctor__expertise__title', 'time', 'amount', 'is_active', 'is_taken']
    search_fields = ['id', 'doctor__id']
    list_filter = ['is_active', 'is_taken']


@register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
