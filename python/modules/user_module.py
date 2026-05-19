from package import fact as p

a=p.fact()
print(a)

import math as m
print(m.copysign(90.1,56.2))
print(m.comb(90,87))

import datetime as dt
print(dt.date.ctime(dt.date(2025,9,2)))
# print(dt.datetime.date(dt.date.day))
print(dt.date.fromisocalendar(year=2020,week=33,day=4))
print(dt.date.day)
print(dt.date.fromtimestamp(2020))
print(dt.date.isoweekday(dt.date(year=2020,month=12,day=5)))
print(dt.date.month)
print(dt.date.today())
print(dt.date.year)

import calendar

print(calendar.isleap(2100))

print(dt.datetime.now())

import calendar as cal

print(cal.month(theyear=2020,themonth=1))

class Test:

    count = 0

    def __init__(self):
       self.count += 1

a = Test()
b = Test()
c = Test()

print(a.count)

