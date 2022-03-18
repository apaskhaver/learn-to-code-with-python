import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class TestRoyalFlushValidator(unittest.TestCase):
    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_straight_cards_with_same_rank_ending_in_ace(self):
        ten_of_clubs = Card(rank = "10", suit = "Clubs")
        jack_of_clubs = Card(rank = "Jack", suit = "Clubs")
        queen_of_clubs = Card(rank = "Queen", suit = "Clubs")
        king_of_clubs =  Card(rank = "King", suit = "Clubs")
        ace_of_clubs =  Card(rank = "Ace", suit = "Clubs")

        cards = [
            Card(rank = "2", suit = "Spades"),
            ten_of_clubs,
            jack_of_clubs,
            queen_of_clubs,
            king_of_clubs,
            ace_of_clubs,
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                ten_of_clubs,
                jack_of_clubs,
                queen_of_clubs,
                king_of_clubs,
                ace_of_clubs
            ]
        )