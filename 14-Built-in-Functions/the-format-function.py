number = 0.123456789

print(format(number, "f"))
print(type(format(number, "f"))) # it's a string

print(format(number, ".2f"))
print(format(number, ".4f")) # rounds it to 4 decimal places

print(format(0.5, "f"))
print(format(0.5, "%"))
print(format(0.5, ".2%"))

print(format(123456789, ","))