from unittest import TestCase
from Board import Board, Tile


class BoardTest(TestCase):
    def setUp(self):
        self.board = Board(19)

    def test_size(self):
        self.assertEqual(19, self.board.size)

    def test_get_info_at(self):
        self.assertEqual(Tile.EMPTY, self.board.get_info_at(0, 0))

    def test_set_info_at(self):
        self.board.set_info_at(0, 0, Tile.ENEMY)
        self.assertEqual(Tile.ENEMY, self.board.get_info_at(0, 0))
