from datetime import datetime

from khayyam import *

date = JalaliDate(datetime.now()).strftime('%A %D %B')
time = JalaliDatetime(datetime.now()).strftime(' %H:%M ')
print(JalaliDatetime(datetime.now()))
print(date, time)
print(JalaliDatetime(datetime.now()).strftime(' %h:%v '))
