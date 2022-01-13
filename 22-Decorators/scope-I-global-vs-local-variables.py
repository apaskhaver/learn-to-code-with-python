age = 18

def fancy_func():
    age = 100
    print(age)

fancy_func() # prints 100
print(age) # prints 18

TAX_RATE = 0.08

def calculate_tax(price):
    return round(price * TAX_RATE, 2)

def calculate_tip(price):
    return round(price * TAX_RATE * 3, 2)

print(calculate_tax(10))
print(calculate_tip(10))