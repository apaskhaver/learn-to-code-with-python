from poker.validators import FiveCardRanksInARowValidator

class StraightValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"

    def is_valid(self):
        return len(self._collections_of_five_straight_cards_in_a_row) >= 1

    def valid_cards(self):
        # Return the straight with highest ranks, which is the
        # last entry in your collection of straights
        return self._collections_of_five_straight_cards_in_a_row[-1]