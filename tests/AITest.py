from unittest import TestCase
from Board import Board, Tile
from Pos import Pos
from AI import AI


class AITest(TestCase):

    def test_evaluation_of_position(self):
        custom_board = Board(3, [
            [Tile.MINE, Tile.EMPTY, Tile.EMPTY],
            [Tile.MINE, Tile.MINE, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT]
        ])
        self.assertRaises(Exception, AI.evaluation_of_position, custom_board, Pos(-1, 0))
        self.assertEqual(1, AI.evaluation_of_position(custom_board, Pos(0, 1)))
        self.assertEqual(2, AI.evaluation_of_position(custom_board, Pos(1, 2)))
