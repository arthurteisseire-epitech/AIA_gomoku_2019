from enum import Enum
from Pos import Pos


class Tile(Enum):
    EMPTY = 0
    MINE = 1
    OPPONENT = 2
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

    def get_row_at(self, pos, distance=0):
        if distance == 0:
            return self.board[pos.y]
        left_x = pos.x - distance
        if left_x < 0:
            left_x = 0
        right_x = pos.x + distance + 1
        if right_x >= self.size:
            right_x = self.size
        return self.board[pos.y][left_x:][:right_x]

    def get_col_at(self, pos, distance=0):
        col = [row[pos.x] for row in self.board]
        if distance == 0:
            return col
        top_y = max(0, pos.y - distance)
        bot_y = min(pos.y + distance + 1, self.size)
        return col[top_y:][:bot_y]

    def get_diagonal_top_left_to_bottom_right(self, pos):
        offset = pos.x - pos.y
        return [row[offset + i] for i, row in enumerate(self.board) if 0 <= offset + i < len(row)]

    def get_diagonal_top_right_to_bottom_left(self, pos):
        offset = pos.y + pos.x
        return [row[offset - i] for i, row in enumerate(self.board) if 0 <= offset - i < len(row)]
