from enum import Enum


class Tile(Enum):
    EMPTY = 0
    OPPONENT = 1
    MINE = 2
    OUT_OF_BOUND = 3


class Board:
    def __init__(self, size, board=None):
        if board is None:
            self.board = [[Tile.EMPTY for i in range(0, size)] for i in range(0, size)]
        else:
            self.board = board
        self.size = size

    def get_info_at(self, x, y):
        if not self.is_in(x, y):
            return Tile.OUT_OF_BOUND
        return self.board[x][y]

    def set_info_at(self, x, y, tile):
        if not self.is_in(x, y):
            return False
        self.board[x][y] = tile
        return True

    def is_in(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size
