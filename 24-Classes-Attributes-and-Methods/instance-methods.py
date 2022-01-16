class Pokemon():
    def __init__(self, name, specialty, health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health
    
    def roar(self):
        print("Raaaaaar!")

    def describe(self):
        print(f"I am {self.name} and I am a {self.specialty} Pokemon.")
    
    def take_damage(self, amount):
        self.health -= amount

    
squirtle = Pokemon("Squirtle", "water")
charmander = Pokemon(name = "Charmander", specialty = "fire", health = 110)

squirtle.roar()
charmander.roar()

squirtle.describe()
charmander.describe()

print(squirtle.health)
squirtle.take_damage(10)
print(squirtle.health)

# can also do this
squirtle.health = 60
print(squirtle.health)

print(charmander.health)