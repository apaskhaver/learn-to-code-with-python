class HighCardValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "High Card"

    def is_valid(self):
        # all the checks for higher ranks have
        # failed, but the player has at least
        # 2 cards: means high card is highest
        # rank.
        return len(self.cards) >= 2

    def valid_cards(self):
        # assuming list is sorted
        # highest card is last.
        # Returns as list.
        return self.cards[-1:]