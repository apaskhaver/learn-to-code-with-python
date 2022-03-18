from poker.validators import FiveCardRanksInARowValidator

class StraightFlushValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"

    def is_valid(self):
        unique_suits_in_next_five_cards = set()

        for five_cards in self._collections_of_five_straight_cards_in_a_row:
            unique_suits_in_next_five_cards = {card.suit for card in five_cards}
        
        return len(unique_suits_in_next_five_cards) == 1
    
    def valid_cards(self):
        # return greatest straight_flush from list of
        # all possible straight flushes (cards already sorted)
        return self._straight_flush_card_batches[-1]

    @property
    def _straight_flush_card_batches(self):
        # iterate over all straights. Check if they're straight
        # flushes with set comprehension. Return list of
        # all straight flushes
        return [
            five_cards for five_cards in self._collections_of_five_straight_cards_in_a_row
            # set comprehension. Each unique suit goes
            # in the set. If len of set is 1, if there
            # is only 1 unique suit among all the straight cards,
            # you have a straight flush. Sets automatically
            # remove duplicates.
            if len({card.suit for card in five_cards}) == 1
        ]