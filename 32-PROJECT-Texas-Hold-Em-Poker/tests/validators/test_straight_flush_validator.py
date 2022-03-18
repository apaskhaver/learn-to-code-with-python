import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class TestStraightFlushValidator(unittest.TestCase):
    def test_validates_there_are_not_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "6", suit = "Clubs"),
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_there_are_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "6", suit = "Clubs"),
            Card(rank = "7", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_determines_there_are_five_consecutive_cards_with_the_same_suit(self):
        three_of_clubs = Card(rank = "3", suit = "Clubs")
        four_of_clubs  = Card(rank = "4", suit = "Clubs")
        five_of_clubs  = Card(rank = "5", suit = "Clubs")
        six_of_clubs   = Card(rank = "6", suit = "Clubs")
        seven_of_clubs =  Card(rank = "7", suit = "Clubs")
        
        cards = [
            three_of_clubs,
            four_of_clubs,
            five_of_clubs,
            six_of_clubs,
            seven_of_clubs,
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                three_of_clubs,
                four_of_clubs,
                five_of_clubs,
                six_of_clubs,
                seven_of_clubs
            ]
        )