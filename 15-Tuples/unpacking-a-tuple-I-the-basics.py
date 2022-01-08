employee = ("Bob", "Johnson", "Manager", 50)

# first_name = employee[0]
# last_name = employee[1]
# position = employee[2]
# age = employee[3]


first_name, last_name, position, age = employee
print(first_name, last_name, position, age) # prints Bob Johnson Manager 50

subject, verb, adjective = ["Python", "is", "fun"]
print(subject, verb, adjective)

a = 5
b = 10
b, a = (a, b)
print(a, b) # prints 10 5

# Right side of equation is evaluated first, locking in
# the values (5, 10) which are then reassigned to the
# variables on the left side of the equals, b and a,
# respectively. This sets b = 5 and a = 10