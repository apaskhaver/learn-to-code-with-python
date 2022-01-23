class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'

# default print includes obj's class and position in memory

c1 = Card("Ace", "Spades")
print(c1) # calls __str__(), Ace of Spades
print(str(c1)) # calls __str__(), Ace of Spades
print(repr(c1)) # calls __repr__(), Card("Ace", "Spades")

print()

c2 = Card("King", "Hearts")
print(c2)
print(str(c2))
print(repr(c2))