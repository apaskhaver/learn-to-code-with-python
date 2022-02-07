from datetime import datetime
# module named datetime, specific class within it
# also named datetime. We're importing the class
# from the module
# if it was just import datetime, you'd have to do
# datetime.datetime to access the class.

print(datetime(1999, 7, 4))
print(datetime(1999, 7, 4, 14))
print(datetime(1999, 7, 4, 14, 16))
print(datetime(1999, 7, 4, 14, 16, 58))

print(datetime(year = 1999, month = 7, day = 4, hour = 14, minute = 16, second = 58))

today = datetime.today()
print(today)
print(datetime.now())
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

print(today.weekday())

same_time_twenty_years_ago = today.replace(year = 2002)
print(same_time_twenty_years_ago)

same_time_in_january = today.replace(month = 1)
print(same_time_in_january)

same_time_jan_1_1999 = today.replace(year = 1999, month = 1, day = 1)
print(same_time_jan_1_1999)