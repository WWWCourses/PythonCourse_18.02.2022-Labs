from datetime import date, time, datetime, timedelta, tzinfo
import pytz

mil = date(2000, 1, 1)
t = time(20, 0, 0)
date_now = datetime.now()

print(mil, t, date_now)

dt = timedelta(days=1, hours=10)
print(mil + dt)
print(date_now)
print(date_now + dt)
print()

print(date_now)
formatted_date = date.strftime(date_now, "%a/%d/%m(%b) - %Y")
print(formatted_date)

print('timestamp = ', date_now.timestamp())
print()
print('timestamp = ', date_now.timestamp())

d1 = datetime.now()
d2 = d1 - timedelta(days=3)
print(d1 - d2)
print(date_now.strftime("%H:%M:%S"))

print(date_now.strftime("%m/%d/%Y"))

d = datetime(2021, 6, 14, 20, 3, 12, 0, tzinfo=pytz.utc)
print(d.tzinfo)


utc = pytz.utc
print(utc)
print(utc.zone)

eastern = pytz.timezone('US/Eastern')
print(eastern)
print(eastern.zone)

gmt = pytz.timezone('Etc/GMT')
print(gmt)

datetime_gmt = datetime.now(gmt)
print(datetime_gmt)
print(date_now)

print(date_now.astimezone(gmt))
print(date_now.astimezone(eastern))

d1 = date_now.astimezone(gmt)
d2 = date_now.astimezone(eastern)
print(d2.time())

print()
dt = datetime(2020, 12, 2, 3, 30 ,0, 23423)
dt1 = eastern.localize(dt)
print(dt1)
print(dt1.time())

from pytz import reference
localtime = reference.LocalTimezone()
print(localtime.tzname(date_now))
