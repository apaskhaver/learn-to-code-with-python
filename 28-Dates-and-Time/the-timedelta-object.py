from datetime import datetime, timedelta

birthday = datetime(1947, 2, 19)
today = datetime.now()

life_span = today - birthday
print(life_span)
print(type(life_span))

print(life_span.total_seconds())

five_hundred_days = timedelta(days = 500, hours = 12)
print(five_hundred_days)

print(five_hundred_days + five_hundred_days)
print(today + five_hundred_days)