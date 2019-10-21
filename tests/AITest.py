from unittest import TestCase
from Board import Board, Tile
from Pos import Pos
from AI import AI
from Weight import Weight


class AITest(TestCase):

    def test_evaluation_of_position_error(self):
        custom_board = Board(3, [
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.MINE, Tile.EMPTY, Tile.EMPTY]
        ])
        self.assertRaises(Exception, AI.evaluation_of_position, custom_board, Pos(-1, 0))

    def test_evaluation_of_position(self):
        custom_board = Board(3, [
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.MINE, Tile.EMPTY, Tile.MINE]
        ])
        self.assertEqual(Weight.OPPONENT + Weight.MINE * 2, AI.evaluation_of_position(custom_board, Pos(0, 0)))
