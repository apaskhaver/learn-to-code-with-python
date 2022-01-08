def accept_stuff(*args):
    print(type(args)) 
    print(args)

accept_stuff()
accept_stuff(1)
accept_stuff(1, 2, 3)
accept_stuff(1, 2, 3, 4, 5, 6)

def my_max(nonsense, *numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    
    return nonsense, max

print(my_max("Shazam", 1))
print(my_max("Hurrah", 1, 2))
print(my_max("Bonanza", 10, 1013, 10))

def my_max_2(*numbers, nonsense):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    
    return max, nonsense

print(my_max_2(1, nonsense = "Shazam"))
print(my_max_2(1, 2, nonsense = "Hurrah"))
print(my_max_2(10, 1013, 10, nonsense = "Bonanza"))