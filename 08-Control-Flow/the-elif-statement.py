def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative!"
    else:
        return "Neither! It's 0."

print(positive_or_negative(5))
print(positive_or_negative(-3))
print(positive_or_negative(0))

def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

print(calculator("add", 3, 4))
print(calculator("subtract", 3, 4))
print(calculator("multiply", 3, 4))
print(calculator("divide", 3, 4))
print(calculator("transmogrify", 3, 4))