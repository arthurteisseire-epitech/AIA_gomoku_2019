from unittest import TestCase
from Board import Board, Tile
from Pos import Pos
from AI import AI


class AlgoTest(TestCase):
    def test_minimax_depth(self):
        custom_board = Board(3, [
            [Tile.OPPO, Tile.MINE, Tile.OPPO],
            [Tile.MINE, Tile.MINE, Tile.OPPO],
            [Tile.MINE, Tile.OPPO, Tile.EMPT]
        ])
        expected = Pos(2, 2)
        actual = AI.next_move(custom_board)
        self.assertEqual(expected, actual, "\nexpected: " + expected.to_string() + "\nactual: " + actual.to_string())

    def test_evaluation_attack(self):
        custom_board = Board(19, [
            [Tile.EMPT, Tile.EMPT, Tile.OPPO, Tile.MINE, Tile.MINE, Tile.MINE, Tile.MINE, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
        ])
        actual = AI.find_best_position(custom_board)
        expected = Pos(0, 7)
        self.assertEqual(expected, actual, "expected: " + expected.to_string() + ", actual: " + actual.to_string())

    def test_evaluation_defense(self):
        custom_board = Board(19, [
            [Tile.EMPT, Tile.MINE, Tile.OPPO, Tile.OPPO, Tile.OPPO, Tile.OPPO, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
        ])
        actual = AI.find_best_position(custom_board)
        expected = Pos(0, 6)
        self.assertEqual(expected, actual, "expected: " + expected.to_string() + ", actual: " + actual.to_string())
