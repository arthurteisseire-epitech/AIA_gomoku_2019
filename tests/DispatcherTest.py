from unittest import TestCase
from Dispatcher import Dispatcher
from Board import Board


class DispatcherTest(TestCase):
    def setUp(self):
        self.dispatcher = Dispatcher(Board(19))

    def test_start(self):
        self.assertEqual("OK", self.dispatcher.dispatch("START 8"))
        self.assertEqual(8, self.dispatcher.board.size)
