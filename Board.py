from enum import Enum


class Tile(Enum):
    EMPTY = 0
    ENEMY = 1
    MINE = 2


class Board:
    def __init__(self, size):
        self.board = [[Tile.EMPTY for i in range(0, size)] for i in range(0, size)]
        self.size = size
