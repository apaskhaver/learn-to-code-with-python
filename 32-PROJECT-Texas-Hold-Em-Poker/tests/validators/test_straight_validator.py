import unittest

from poker.card import Card
from poker.validators import StraightValidator

class TestStraightCardValidator(unittest.TestCase):
    def setUp(self):
        two_of_spades          = Card(rank = "2", suit = "Spades")
        six_of_hearts          = Card(rank = "6", suit = "Hearts")
        self.seven_of_diamonds = Card(rank = "7", suit = "Diamonds")
        self.eight_of_spades   = Card(rank = "8", suit = "Spades")
        self.nine_of_clubs     = Card(rank = "9", suit = "Clubs")
        self.ten_of_clubs      = Card(rank = "10", suit = "Clubs")
        self.jack_of_hearts    = Card(rank = "Jack", suit = "Hearts")
        
        self.cards = [
            two_of_spades,
            six_of_hearts,
            self.seven_of_diamonds,
            self.eight_of_spades,
            self.nine_of_clubs,
            self.ten_of_clubs,
            self.jack_of_hearts
        ]

    def test_determines_if_there_are_five_cards_in_a_row(self):
        # we tested all the way in the beginning
        # that the hand is sorted, so we can assume
        # cards are sorted.
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds")
        ]

        # want to use local variable cards here,
        # not self.cards above in setUp
        validator = StraightValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_returns_five_highest_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven_of_diamonds,
                self.eight_of_spades,
                self.nine_of_clubs,
                self.ten_of_clubs,
                self.jack_of_hearts
            ]
        )