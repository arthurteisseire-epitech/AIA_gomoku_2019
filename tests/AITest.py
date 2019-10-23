from unittest import TestCase
from Board import Board, Tile
from Pos import *
from AI import AI


class AITest(TestCase):
    def test_evaluation_of_best_position(self):
        custom_board = Board(3, [
            [Tile.OPPONENT, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY]
        ])
        expected = Pos(1, 1)
        actual = AI.find_best_position(custom_board)
        self.assertEqual(expected, actual, "\nexpected: " + expected.to_string() + "\ngot: " + actual.to_string())
