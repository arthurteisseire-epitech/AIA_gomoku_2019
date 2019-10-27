from unittest import TestCase
from board.Board import Board, Tile
from board.Pos import Pos


class BoardTest(TestCase):
    def setUp(self):
        self.board = Board(19)
        self.custom_board = Board(4, [
            [Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE],
            [Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE],
            [Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE],
            [Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE],
        ])

    def test_custom_board(self):
        self.assertEqual(Tile.MINE, self.custom_board.get_info_at(Pos(0, 0)))
        self.assertEqual(Tile.OPPO, self.custom_board.get_info_at(Pos(2, 2)))
        self.assertEqual(Tile.EMPT, self.custom_board.get_info_at(Pos(1, 1)))

    def test_size(self):
        self.assertEqual(19, self.board.size)

    def test_is_in(self):
        self.assertTrue(self.board.is_in(Pos(0, 0)))
        self.assertFalse(self.board.is_in(Pos(-1, -1)))

        self.assertTrue(self.board.is_in(Pos(18, 18)))
        self.assertFalse(self.board.is_in(Pos(19, 19)))

    def test_get_info_at(self):
        self.assertEqual(Tile.EMPT, self.board.get_info_at(Pos(0, 0)))
        self.assertEqual(Tile.EMPT, self.board.get_info_at(Pos(18, 18)))

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
        self.assertTrue(self.board.set_info_at(Pos(0, 0), Tile.OPPO))
        self.assertTrue(self.board.set_info_at(Pos(18, 18), Tile.MINE))
        self.assertEqual(Tile.OPPO, self.board.get_info_at(Pos(0, 0)))
        self.assertEqual(Tile.MINE, self.board.get_info_at(Pos(18, 18)))

    def test_get_row_at(self):
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE], self.custom_board.get_row_at(Pos(0, 0)))
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE], self.custom_board.get_row_at(Pos(1, 1)))
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE], self.custom_board.get_row_at(Pos(3, 3)))

    def test_get_row_at_with_distance(self):
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO], self.custom_board.get_row_at(Pos(0, 1), 1))
        self.assertEqual([Tile.EMPT, Tile.OPPO, Tile.MINE], self.custom_board.get_row_at(Pos(0, 2), 1))

        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE], self.custom_board.get_row_at(Pos(0, 2), 2))
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE], self.custom_board.get_row_at(Pos(0, 1), 2))
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE], self.custom_board.get_row_at(Pos(0, 0), 3))
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE], self.custom_board.get_row_at(Pos(0, 3), 3))

    def test_get_col_at(self):
        self.assertEqual([Tile.EMPT, Tile.EMPT, Tile.EMPT, Tile.EMPT], self.custom_board.get_col_at(Pos(0, 1)))

    def test_get_col_at_with_distance(self):
        self.assertEqual([Tile.MINE, Tile.MINE], self.custom_board.get_col_at(Pos(0, 0), 1))
        self.assertEqual([Tile.MINE, Tile.MINE, Tile.MINE], self.custom_board.get_col_at(Pos(1, 0), 1))
        self.assertEqual([Tile.MINE, Tile.MINE, Tile.MINE, Tile.MINE], self.custom_board.get_col_at(Pos(1, 0), 3))
        self.assertEqual([Tile.EMPT, Tile.EMPT, Tile.EMPT], self.custom_board.get_col_at(Pos(1, 1), 1))

    def test_get_diagonal_top_left_to_bottom_right(self):
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(0, 0)))
        self.assertEqual(self.custom_board.get_principal_diagonal(Pos(0, 0)),
                         self.custom_board.get_principal_diagonal(Pos(1, 1)))
        self.assertEqual(self.custom_board.get_principal_diagonal(Pos(0, 0)),
                         self.custom_board.get_principal_diagonal(Pos(2, 2)))
        self.assertEqual(self.custom_board.get_principal_diagonal(Pos(0, 0)),
                         self.custom_board.get_principal_diagonal(Pos(3, 3)))

        self.assertEqual([Tile.OPPO, Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(0, 2)))
        self.assertEqual(self.custom_board.get_principal_diagonal(Pos(0, 2)),
                         self.custom_board.get_principal_diagonal(Pos(1, 3)))

        self.assertEqual([Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(0, 3)))

        self.assertEqual([Tile.MINE, Tile.EMPT],
                         self.custom_board.get_principal_diagonal(Pos(3, 1)))

    def test_get_diagonal_top_left_to_bottom_right_with_distance(self):
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(0, 0), 3))
        self.assertEqual([Tile.MINE, Tile.EMPT],
                         self.custom_board.get_principal_diagonal(Pos(0, 0), 1))
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO],
                         self.custom_board.get_principal_diagonal(Pos(1, 1), 1))

        self.assertEqual([Tile.OPPO, Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(1, 3), 1))
        self.assertEqual([Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(3, 0), 1))
        self.assertEqual([Tile.EMPT, Tile.OPPO],
                         self.custom_board.get_principal_diagonal(Pos(3, 2), 1))
        self.assertEqual([Tile.OPPO, Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(3, 3), 1))
        self.assertEqual([Tile.EMPT, Tile.OPPO, Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(3, 3), 2))
        self.assertEqual([Tile.MINE, Tile.EMPT, Tile.OPPO, Tile.MINE],
                         self.custom_board.get_principal_diagonal(Pos(3, 3), 12))

    def test_get_diagonal_top_right_to_bottom_left(self):
        self.assertEqual([Tile.MINE, Tile.OPPO, Tile.EMPT, Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(3, 0)))
        self.assertEqual(self.custom_board.get_counter_diagonal(Pos(3, 0)),
                         self.custom_board.get_counter_diagonal(Pos(1, 2)))
        self.assertEqual(self.custom_board.get_counter_diagonal(Pos(3, 0)),
                         self.custom_board.get_counter_diagonal(Pos(2, 1)))
        self.assertEqual(self.custom_board.get_counter_diagonal(Pos(3, 0)),
                         self.custom_board.get_counter_diagonal(Pos(0, 3)))

        self.assertEqual([Tile.OPPO, Tile.EMPT, Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(2, 0)))
        self.assertEqual(self.custom_board.get_counter_diagonal(Pos(2, 0)),
                         self.custom_board.get_counter_diagonal(Pos(1, 1)))
        self.assertEqual(self.custom_board.get_counter_diagonal(Pos(2, 0)),
                         self.custom_board.get_counter_diagonal(Pos(0, 2)))

        self.assertEqual([Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(3, 3)))

    def test_get_diagonal_top_right_to_bottom_left_with_distance(self):
        self.assertEqual([Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(0, 0), 3))
        self.assertEqual([Tile.EMPT, Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(0, 1), 1))
        self.assertEqual([Tile.OPPO, Tile.EMPT],
                         self.custom_board.get_counter_diagonal(Pos(0, 2), 1))

        self.assertEqual([Tile.MINE, Tile.OPPO, Tile.EMPT, Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(3, 0), 3))
        self.assertEqual([Tile.EMPT, Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(3, 0), 1))
        self.assertEqual([Tile.MINE, Tile.OPPO],
                         self.custom_board.get_counter_diagonal(Pos(0, 3), 1))
        self.assertEqual([Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(3, 3), 1))

        self.assertEqual([Tile.MINE, Tile.OPPO, Tile.EMPT],
                         self.custom_board.get_counter_diagonal(Pos(1, 2), 1))
        self.assertEqual([Tile.OPPO, Tile.EMPT, Tile.MINE],
                         self.custom_board.get_counter_diagonal(Pos(2, 1), 1))
