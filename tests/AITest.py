from unittest import TestCase
from board.Board import Board, Tile
from board.Pos import *
from ai.AI import AI


class AITest(TestCase):
    def test_find_best_position_one_stone(self):
        custom_board = Board(3, [
            [Tile.OPPONENT, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY]
        ])
        expected = Pos(1, 1)
        actual = AI.find_best_position(custom_board)
        self.assertEqual(expected, actual, "\nexpected: " + expected.to_string() + "\ngot: " + actual.to_string())

    def test_find_best_position_two_stone(self):
        custom_board = Board(3, [
            [Tile.OPPONENT, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.MINE, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT]
        ])
        expected = Pos(0, 1)
        actual = AI.find_best_position(custom_board)
        self.assertEqual(expected, actual, "\nexpected: " + expected.to_string() + "\ngot: " + actual.to_string())
