from khayyam import JalaliDate, JalaliDatetime

from doctor.models import Visit


def fix_datetime(date, hour, minute):
    tmpdate = date.split('-')
    year = tmpdate[0]
    month = tmpdate[1].removeprefix('0')
    day = tmpdate[2].removeprefix('0')
    return JalaliDatetime(year=int(year), month=int(month), day=int(day), hour=int(hour),
                          minute=int(minute)).todatetime()


def set_visit(request, doctor):
    date = request.POST.get('date')
    hour = request.POST.get('hour')
    minute = request.POST.get('minute')
    amount = request.POST.get('amount')
    date_time = fix_datetime(date=date, hour=hour, minute=minute)
    Visit.objects.create(
        doctor=doctor,
        amount=amount,
        time=date_time
    )
