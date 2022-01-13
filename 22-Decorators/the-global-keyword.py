# x = 10

def change_stuff():
    global x
    x = 15

change_stuff()
print(x) # prints 15 because global x enters function
