from datetime import datetime

today = datetime.today()

print(today.strftime("%m")) # month as a number
print(today.strftime("%m %d")) # month space day as numbers
print(today.strftime("%m/%d/%Y")) # month/day/4 digit year as numbers
print(today.strftime("%m-%d-%Y")) # month-day-4 digit year as numbers

print(today.strftime("%Y-%m-%d")) # different order
print(today.strftime("%y-%m-%d")) # 2 digit year

print(today.strftime("%A")) # weekday as a string
print(today.strftime("%B")) # month as a string