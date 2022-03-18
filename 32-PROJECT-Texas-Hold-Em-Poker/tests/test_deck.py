import unittest
from unittest.mock import patch

from poker.card import Card
from poker.deck import Deck

class TestDeck(unittest.TestCase):
    def test_has_length_that_is_equal_to_count_of_cards(self):
        deck = Deck()

        self.assertEqual(
            len(deck),
            0
        )
        
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_adds_cards_to_its_collection(self):
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])
        self.assertEqual(
            deck.cards,
            [card]
        )

    def test_removes_specified_number_of_cards_from_deck(self):
        ace_of_spades     = Card(rank = "Ace", suit = "Spades")
        eight_of_diamonds = Card(rank = "8", suit = "Diamonds")
        
        cards = [ace_of_spades, eight_of_diamonds]

        deck = Deck()
        deck.add_cards(cards)

        # assert we returned the removed cards
        self.assertEqual(
            deck.remove_cards(1),
            [ace_of_spades]
        )

        # assert the removed cards were
        # deleted from the cards list
        self.assertEqual(
            deck.cards,
            [eight_of_diamonds]
        )

    # whenever our program calls shuffle,
    # step in and use a mock object / method instead
    # which we will call mock_shuffle, passed in below.
    # Some say @patch showcases dependencies in code:
    # you couldn't mock a call to an outside module
    # if there were no dependencies in the obj
    # you're testing in the first place.
    @patch("random.shuffle")
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        deck = Deck()
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds"),
        ]

        deck.add_cards(cards)

        deck.shuffle()

        # assert the mock_shuffle was called
        # with cards as an argument; that it's
        # "shuffling" cards
        mock_shuffle.assert_called_once_with(cards)