def add(a, b):
    print(a + b)
# add() # runs an error because no arguments were passed. However...

def add2(a = 4, b = 5):
    print(a + b)
add2() # will not run an error; the default values of a = 4 and b = 5 will be passed into the function

