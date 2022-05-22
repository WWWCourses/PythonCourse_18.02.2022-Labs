import datetime as dt
import time
import pytz

# get current time ()
# now = dt.datetime.now()
# print(now)


# # get epoch time
# t = time.time()
# print(t)

# lunch_time = dt.time(hour=12, minute=0, second=0)
# print(lunch_time)

# now = dt.datetime.now().time()
# print(now.hour)
# print(now.tzname())

# birth_date_str = input('Enter birth date [YYYY-MM-DD]:')
# birth_date = dt.date.fromisoformat(birth_date_str)

# print(birth_date.year)

# YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
# dt1 = dt.datetime.fromisoformat('1999-12-28.17:34')
# print(dt1.day)

# get week day
# now = dt.datetime.now()
# wday = now.weekday()
# print(wday)

# TASK: get weekday of user birth day
# birth_date_str = '2021-05-22'
# birth_date = dt.date.fromisoformat(birth_date_str)

# weekday_map = {
# 	'0':'Monday',
# 	'5': 'Saturday'
# }

# i = 0
# print(weekday_map[str(i)])

# weekday_map = ['Monday', 'Saturday']
# i = 0
# birth_date_wd = birth_date.weekday()

# get datetime object from string (DD/MM/YYYY)
# dt_obj = dt.datetime.strptime('22/05/2022','%d/%m/%Y')
# print(dt_obj)


# due_date = dt.date(2023, 6, 1)
# current_date = dt.datetime.now().date()

# td = due_date - current_date
# print(td.total_seconds())

# now = dt.datetime.now(tz='UTC')
# print(now)


# utc = pytz.utc
# print(utc)
# print(utc.zone)

# eastern = pytz.timezone('US/Eastern')
# print(eastern)
# print(eastern.zone)