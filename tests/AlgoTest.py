from unittest import TestCase
from board.Board import Board, Tile
from board.Pos import Pos
from ai.AI import AI


class AlgoTest(TestCase):
    def test_minimax_depth(self):
        custom_board = Board(3, [
            [Tile.OPPONENT, Tile.MINE, Tile.OPPONENT],
            [Tile.MINE, Tile.MINE, Tile.OPPONENT],
            [Tile.MINE, Tile.OPPONENT, Tile.EMPTY]
        ])
        expected = Pos(2, 2)
        actual = AI.next_move(custom_board)
        self.assertEqual(expected, actual, "\nexpected: " + expected.to_string() + "\nactual: " + actual.to_string())
