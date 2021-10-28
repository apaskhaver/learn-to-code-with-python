def subtract(a, b):
    print("The difference of", a, "and", b, "is", a - b)
subtract(3, 4)
subtract(b = 3, a = 4)

def add(a, b, c):
    print("The sum of", a, "and", b, "and", c, "is", a + b + c)
add(4, 2, 3)
add(a = 4, b = 2, c = 3)
add(4, c = 2, b = 3)
# add(4, 2, b=3) # runs the error "got multiple values for argument b" because positionally, b=2
add(4, 2, c = 3)