class Book():
    # default price of 14.99 when price attribute not provided
    # otherwise, self.price is set to the passed-in price
    def __init__(self, title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price

animal_farm = Book("Animal Farm", "George Orwell", 19.99)
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")

print(animal_farm.price) # 19.99
print(gatsby.price) # 14.99

atlas = Book(title = "Atlas Shrugged", author = "Ayn Rand")
jude = Book(author = "Thomas Hardy", price = 24.99, title = "Jude the Obscure")