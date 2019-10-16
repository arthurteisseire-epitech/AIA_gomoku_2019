from unittest import TestCase
from Board import Board, Tile
from Pos import Pos


class BoardTest(TestCase):
    def setUp(self):
        self.board = Board(19)

    def test_custom_board(self):
        custom_board = Board(3, [
            [Tile.MINE, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.OPPONENT]
        ])
        self.assertEqual(Tile.MINE, custom_board.get_info_at(Pos(0, 0)))
        self.assertEqual(Tile.OPPONENT, custom_board.get_info_at(Pos(2, 2)))
        self.assertEqual(Tile.EMPTY, custom_board.get_info_at(Pos(1, 1)))

    def test_size(self):
        self.assertEqual(19, self.board.size)

    def test_is_in(self):
        self.assertTrue(self.board.is_in(Pos(0, 0)))
        self.assertFalse(self.board.is_in(Pos(-1, -1)))

        self.assertTrue(self.board.is_in(Pos(18, 18)))
        self.assertFalse(self.board.is_in(Pos(19, 19)))

    def test_get_info_at(self):
        self.assertEqual(Tile.EMPTY, self.board.get_info_at(Pos(0, 0)))
        self.assertEqual(Tile.EMPTY, self.board.get_info_at(Pos(18, 18)))

    def test_get_info_out_of_bound(self):
        self.assertEqual(Tile.OUT_OF_BOUND, self.board.get_info_at(Pos(-1, 0)))
        self.assertEqual(Tile.OUT_OF_BOUND, self.board.get_info_at(Pos(0, -1)))
        self.assertEqual(Tile.OUT_OF_BOUND, self.board.get_info_at(Pos(0, 19)))
        self.assertEqual(Tile.OUT_OF_BOUND, self.board.get_info_at(Pos(19, 0)))

    def test_set_info_out_of_bound(self):
        self.assertFalse(self.board.set_info_at(Pos(-1, 0), Tile.MINE))
        self.assertFalse(self.board.set_info_at(Pos(19, 0), Tile.MINE))
        self.assertFalse(self.board.set_info_at(Pos(0, -1), Tile.MINE))
        self.assertFalse(self.board.set_info_at(Pos(0, 19), Tile.MINE))

    def test_set_info_at(self):
        self.assertTrue(self.board.set_info_at(Pos(0, 0), Tile.OPPONENT))
        self.assertTrue(self.board.set_info_at(Pos(18, 18), Tile.MINE))
        self.assertEqual(Tile.OPPONENT, self.board.get_info_at(Pos(0, 0)))
        self.assertEqual(Tile.MINE, self.board.get_info_at(Pos(18, 18)))
