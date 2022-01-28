class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        return f"{self.name} is enjoying {food}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        # same as Animal.__init__(name)
        # Better to use super() b/c if Animal class's name changes,
        # won't break code.
        self.breed = breed

watson = Dog("Watson", "Golden Retriever")
print(watson.eat("bacon")) # Watson is enjoying bacon
print(watson.name) # Watson
print(watson.breed) # Golden Retriever