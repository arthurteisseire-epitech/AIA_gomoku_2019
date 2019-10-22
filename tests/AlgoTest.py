from unittest import TestCase
from Algo import Algo


def evaluation_function():
    return 3


class AlgoTest(TestCase):

    def test_minimax(self):
        self.assertEqual(evaluation_function(), Algo.minimax(evaluation_function, 0))
