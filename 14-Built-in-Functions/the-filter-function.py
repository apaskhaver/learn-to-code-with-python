animals = ["elephant", "horse", "cat", "giraffe", "cheetah", "dog"]
long_animals = [animal for animal in animals if len(animal) > 5]
print(long_animals)

def is_long_animal(animal):
    return len(animal) > 5

print(filter(is_long_animal, animals))
print(list(filter(is_long_animal, animals)))