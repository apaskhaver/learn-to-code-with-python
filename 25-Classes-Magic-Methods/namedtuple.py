import collections

Book = collections.namedtuple("Book", ["title", "author"])
# collections.namedtuple("Book", "title author"])

# attributes given in the order they're declared in the namedtuple()
# or through keyword args
animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(author = "F. Scott Fitzgerald", title = "The Great Gatsby")

print(animal_farm[0]) # Animal Farm
print(gatsby[0]) # The Great Gatsby (order preserved as declared in namedtuple())
print(animal_farm.title) # Animal Farm
print(gatsby.author) # F. Scott Fitzgerald