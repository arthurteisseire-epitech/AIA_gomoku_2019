from unittest import TestCase
from Board import Board, Tile
from Pos import *
from AI import AI


class AITest(TestCase):
    def test_find_best_position_one_stone(self):
        custom_board = Board(3, [
            [Tile.OPPO, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT]
        ])
        expected = Pos(1, 1)
        actual = AI.find_best_position(custom_board)
        self.assertEqual(expected, actual, "\nexpected: " + expected.to_string() + "\ngot: " + actual.to_string())

    def test_find_best_position_two_stone(self):
        custom_board = Board(3, [
            [Tile.OPPO, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.MINE, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.OPPO]
        ])
        expected = Pos(0, 1)
        actual = AI.find_best_position(custom_board)
        self.assertEqual(expected, actual, "\nexpected: " + expected.to_string() + "\ngot: " + actual.to_string())
