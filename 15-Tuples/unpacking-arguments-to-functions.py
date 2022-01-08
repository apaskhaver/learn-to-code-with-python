def product(a, b):
    return a * b

print(product(3, 5))

numbers = (3, 5)
print(product(*numbers))
# expands the tuple into the requisite number of needed arguments
# No error.

print(dir(tuple))
print()
print(dir(list))