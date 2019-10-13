from enum import Enum


class Tile(Enum):
    EMPTY = 0
    ENEMY = 1
    MINE = 2
    OUT_OF_BOUND = 3


class Board:
    def __init__(self, size):
        self.board = [[Tile.EMPTY for i in range(0, size)] for i in range(0, size)]
        self.size = size

    def get_info_at(self, x, y):
        if not self.is_in(x, y):
            return Tile.OUT_OF_BOUND
        return self.board[x][y]

    def set_info_at(self, x, y, tile):
        if self.is_in(x, y):
            self.board[x][y] = tile
            return True
        return False

    def is_in(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size
