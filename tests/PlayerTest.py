from unittest import TestCase
from Player import Player


class PlayerTest(TestCase):
    def test_player_initialisation(self):
        self.assertEqual(Player.MINE, Player(True))
        self.assertEqual(Player.OPPONENT, Player(False))
