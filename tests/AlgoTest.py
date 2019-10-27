from unittest import TestCase
from board.Board import Board, Tile
from board.Pos import Pos
from ai.Player import Player
from ai.Evaluation import Evaluation
from ai.AI import AI


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

    def test_evaluation_easy(self):
        custom_board = Board(19, [
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.MINE, Tile.MINE, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.OPPO, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
            [Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.OPPO, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT],
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
        actual = Evaluation.evaluation_board(custom_board, Player.MINE)
        self.assertEqual(actual, 64)
