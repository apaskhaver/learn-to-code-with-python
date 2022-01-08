employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, *details = employee
# Asterisk indicates to Python that, while it's unpacking,
# It's going to store 1 or more elements in a list.

print(first_name, last_name, details)
# prints Bob Johnson ["Manager", 50]

*names, position, age = employee
print(names, position, age)
# prints ["Bob", "Johnson"] Manager 50

first_name, *details, age = employee
print(first_name, details, age)
# prints Bob ["Johnson", "Manager"] 50

first_name, last_name, position, *details = employee
print(first_name, last_name, position, details)