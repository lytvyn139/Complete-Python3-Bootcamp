import datetime

#2:20 am
mytime = datetime.time(2,20) 
print(mytime)
print(f'hour: {mytime.hour} minute: {mytime.minute} microsecond: {mytime.minute}')

mytime = datetime.time(13,20,1,20) 
#13:20:01.000020
print(mytime)               

today = datetime.date.today()
#2020-06-30
print(f'year: {today.year} month: {today.month} day: {today.day}') 

#Tue Jun 30 00:00:00 2020
print(today.ctime()) 


from datetime import datetime
#2021-10-03 14:20:01

mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)

mydatetime = mydatetime.replace(year=2020)
print(mydatetime)

from datetime import date
#DATE
date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)

result = date1 - date2
print(result ) #356 days
print(type(result)) #datetime.timedelta

print(result.days)

#task: find out how long user was logged in
datetime1 = datetime(2021, 11, 3, 22,0)
datetime2 = datetime(2021, 11, 3, 12,0)
print(datetime1 - datetime2) 




