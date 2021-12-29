# numbers = [3, 4, 5, 6, 7]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(number)
# print(squares)

numbers = [3, 4, 5, 6, 7]
squares = [number ** 2 for number in numbers]
print(squares) # prints [9, 16, 25, 36, 49]

rivers = ["Amazon", "Nile", "Yangtze"]
print([len(river) for river in rivers]) # prints [6, 4, 7]

expressions = ["Hi", "Hello", "Good day"]
print([expression.upper() for expression in expressions])

decimals = [4.95, 3.28, 1.08]
print([int(decimal) for decimal in decimals])