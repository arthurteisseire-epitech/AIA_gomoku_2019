from enum import Enum
from Pos import Pos


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

    def get_info_at(self, pos: Pos):
        if not self.is_in(pos):
            return Tile.OUT_OF_BOUND
        return self.board[pos.y][pos.x]

    def set_info_at(self, pos: Pos, tile):
        if not self.is_in(pos):
            return False
        self.board[pos.y][pos.x] = tile
        return True

    def is_in(self, pos: Pos):
        return 0 <= pos.x < self.size and 0 <= pos.y < self.size

    def get_row_at(self, y):
        return self.board[y]

    def get_col_at(self, x):
        return [row[x] for row in self.board]

    def get_diagonal_top_left_to_bottom_right(self, pos):
        initial_x = abs(pos.x - pos.y)
        res = []
        for i in range(0, self.size - initial_x):
            res.append(self.board[i][initial_x + i])
        return res
