import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.hand import Hand
from poker.player import Player

class TestPlayer(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name = "Boris", hand = hand)
        
        self.assertEqual(player.name, "Boris")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        # arbitrary return value

        player = Player(name = "Boris", hand = mock_hand)
        
        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )

        # when .best_hand() called on player,
        # we expect .best_hand will call hand's 
        # .best_rank() method. We want to know
        # that best_rank is called and
        # that it returns something.
        # Technically, the above assertEqual
        # implicitly guarantees best_hand() called
        # best_rank() and returned something,
        # but there's no harm making it explicit
        # here.
        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Kimberly", hand = mock_hand)

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds")
        ]

        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)

    def test_decides_to_continue_or_drop_out_of_game(self):
        player = Player(name = "Sharon", hand = Hand())
        self.assertEqual(
            player.wants_to_fold(),
            False
        )

    def test_is_sorted_by_best_hand(self):
        mock_hand1 = MagicMock()

        # cards / names are irrelevant, we sort by index
        mock_hand1.best_rank.return_value = (0, "Royal Flush", [])

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (2, "Four of a Kind", [])

        player1 = Player(name = "Kimberley", hand = mock_hand1)
        player2 = Player(name = "Debbie", hand = mock_hand2)

        players = [player1, player2]

        self.assertEqual(
            max(players),
            player1
        )