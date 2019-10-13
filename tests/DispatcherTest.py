from unittest import TestCase
from Dispatcher import Dispatcher


class DispatcherTest(TestCase):
    def test_start(self):
        self.assertEqual("OK", Dispatcher.dispatch("START 19"))

    def test_restart(self):
        self.assertEqual("OK", Dispatcher.dispatch("RESTART"))
