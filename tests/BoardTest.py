from unittest import TestCase
from Board import Board, Tile


class BoardTest(TestCase):
    def setUp(self):
        self.board = Board(19)

    def test_custom_board(self):
        toto = Board(3, [
            [Tile.MINE, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT]
        ])
        self.assertEqual(Tile.MINE, toto.get_info_at(0, 0))
        self.assertEqual(Tile.OPPONENT, toto.get_info_at(2, 2))
        self.assertEqual(Tile.EMPTY, toto.get_info_at(1, 1))

    def test_size(self):
        self.assertEqual(19, self.board.size)

    def test_is_in(self):
        self.assertTrue(self.board.is_in(0, 0))
        self.assertFalse(self.board.is_in(-1, -1))

        self.assertTrue(self.board.is_in(18, 18))
        self.assertFalse(self.board.is_in(19, 19))

    def test_get_info_at(self):
        self.assertEqual(Tile.EMPTY, self.board.get_info_at(0, 0))
        self.assertEqual(Tile.EMPTY, self.board.get_info_at(18, 18))

    def test_get_info_out_of_bound(self):
        self.assertEqual(Tile.OUT_OF_BOUND, self.board.get_info_at(-1, 0))
        self.assertEqual(Tile.OUT_OF_BOUND, self.board.get_info_at(0, -1))
        self.assertEqual(Tile.OUT_OF_BOUND, self.board.get_info_at(0, 19))
        self.assertEqual(Tile.OUT_OF_BOUND, self.board.get_info_at(19, 0))

    def test_set_info_out_of_bound(self):
        self.assertFalse(self.board.set_info_at(-1, 0, Tile.MINE))
        self.assertFalse(self.board.set_info_at(19, 0, Tile.MINE))
        self.assertFalse(self.board.set_info_at(0, -1, Tile.MINE))
        self.assertFalse(self.board.set_info_at(0, 19, Tile.MINE))

    def test_set_info_at(self):
        self.assertTrue(self.board.set_info_at(0, 0, Tile.OPPONENT))
        self.assertTrue(self.board.set_info_at(18, 18, Tile.MINE))
        self.assertEqual(Tile.OPPONENT, self.board.get_info_at(0, 0))
        self.assertEqual(Tile.MINE, self.board.get_info_at(18, 18))
