numbers = [4, 8, 15, 16, 23, 42]

# list comprehension, preferred to mapping
cubes = [number ** 3 for number in numbers]
print(cubes)

# mapping
def cube(number):
    return number ** 3

# into map, pass the function and the iterable on which you want the function
# to be performed
print(map(cube, numbers))
print(list(map(cube, numbers)))

animals = ["cat", "bear", "zebra", "donkey", "cheetah"]
print(list(map(len, animals)))