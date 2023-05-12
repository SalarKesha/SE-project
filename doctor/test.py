from datetime import datetime

from khayyam import *

date = JalaliDate(datetime.now()).strftime('%A %D %B')
time = JalaliDatetime(datetime.now()).strftime(' %H:%M ')
# print(JalaliDatetime(datetime.now()))
# print(date, time)
# print(JalaliDatetime(datetime.now()).strftime(' %h:%v '))
# ipt = '1402-02-22'
# time = '1:0'
# tmp = ipt.split('-')
# tmptime = time.split(':')
# hour = tmptime[0]
# minute = tmptime[1]
# year = tmp[0]
# month = tmp[1].removeprefix('0')
# day = tmp[2].removeprefix('0')
# print(JalaliDatetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute)).todatetime())
