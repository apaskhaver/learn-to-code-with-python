from xml.etree.ElementTree import SubElement


print(type(1))

print(isinstance(1, int))
print(isinstance({"a": 1}, dict))
print(isinstance([], list))
print(isinstance([], int))

print()

print(isinstance(1, object)) # everything in Python inherits from obj
print(isinstance(3.4, object))
print(isinstance(str, object)) 
print(isinstance(max, object))
print(isinstance([], (int, list, dict)))

print()

class Person():
    pass

class Superhero(Person):
    pass

arnold = Person()
boris = Superhero()

print(isinstance(boris, Superhero))
print(isinstance(boris, Person))
print(isinstance(arnold, Person))
print(isinstance(arnold, Superhero))

print()
print()

print(issubclass(Superhero, Person))
print(issubclass(Person, Superhero))
print(issubclass(Person, (str, int)))
print(issubclass(Superhero, (object, Person)))