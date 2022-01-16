class Example():
    data = "Class attribute"

e1 = Example()
e2 = Example()

print(e1.data)
print(e2.data)

print()

# sets an instance attribute with the name of data
# on e1. e1 now has an instance attribute and a class
# attribute with the same name, so if .data is called,
# e1 will access the instance attribute first.
e1.data = "Instance attribute"

print(e1.data)
print(e2.data)

print()

del e1.data # removes the data instance attribute from e1

print(e1.data)
print(e2.data)