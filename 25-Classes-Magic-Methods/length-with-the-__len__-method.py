import collections

Book = collections.namedtuple("Book", ["title", "author"])

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(author = "F. Scott Fitzgerald", title = "The Great Gatsby")

class Library():
    def __init__(self, *books):
        self.books = books # books will be a tuple b/c of *
        self.librarians = []

    def __len__(self):
        return len(self.books)

l1 = Library(animal_farm)
l2 = Library(animal_farm, gatsby)
print(len(l1))
print(len(l2))