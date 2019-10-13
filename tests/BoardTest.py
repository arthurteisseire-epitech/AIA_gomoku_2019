from unittest import TestCase
from Board import Board


class BoardTest(TestCase):
    def setUp(self):
        self.board = Board(19)

    def test_size(self):
        self.assertEqual(19, self.board.size)
