# import datetime
from datetime import date 

birthday = date(1991, 4, 12)
print(birthday)
print(type(birthday))

moon_landing = date(year = 1969, month = 7, day = 20)
print(moon_landing)

# date(2025, 15, 10) # invalid, months must be between 1 - 12
# date(2020, 1, 35) # invalid, days must be between the days of the specified month

print(birthday.year)
print(birthday.month)
print(birthday.day)

# date obj are immutable
# birthday.year = 2000

today = date.today() # class method that returns a date obj of today's date
print(today)
print(type(today))