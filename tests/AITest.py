from unittest import TestCase
from Board import Board, Tile
from Pos import *
from AI import AI
from Weight import Weight


class AITest(TestCase):

    def test_evaluation_of_position_error(self):
        custom_board = Board(3, [
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.MINE, Tile.EMPTY, Tile.EMPTY]
        ])
        self.assertEqual(0, Weight.evaluation_of_position(custom_board, Pos(-1, 0)))

    def test_evaluation_of_position(self):
        custom_board = Board(3, [
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.MINE, Tile.EMPTY, Tile.MINE]
        ])
        self.assertEqual(8, Weight.evaluation_of_position(custom_board, Pos(0, 0)))

    def test_evaluation_of_best_position(self):
        custom_board = Board(3, [
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.MINE, Tile.EMPTY, Tile.MINE]
        ])
        expected = Pos(2, 1)
        actual = AI.find_best_positions(custom_board)[0].pos
        self.assertEqual(expected, actual, "\nexpected: " + expected.to_string() + "\ngot: " + actual.to_string())
