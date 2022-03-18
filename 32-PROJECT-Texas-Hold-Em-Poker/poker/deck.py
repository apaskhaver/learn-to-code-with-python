import random
# Deck is now coupled to the random module.
# If we wanted to inject this dependency,
# we could pass in a shuffle_func as an arg
# to the __init__. There could be multiple
# mathematical ways of shuffling something
# that oughn't necessarily be bound to
# the shuffling function of the random module.

class Deck():
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_cards(self, number):
        cards_to_remove = self.cards[ : number]
        del self.cards[ : number]
        return cards_to_remove

    def shuffle(self):
        random.shuffle(self.cards)

    