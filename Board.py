from enum import Enum
from Pos import Pos


class Tile(Enum):
    EMPT = 0
    MINE = 1
    OPPO = 2
    OUT_OF_BOUND = 3


class Board:
    def __init__(self, size, board=None):
        if board is None:
            self.board = [[Tile.EMPT for i in range(0, size)] for i in range(0, size)]
        else:
            self.board = board
        self.size = size

    def display(self):
        print("----------------\nBoard:")
        for row in self.board:
            print(*row)
        print("----------------")

    def is_full(self):
        for row in self.board:
            if len(list(filter(lambda tile: tile == Tile.EMPT, row))) > 0:
                return False
        return True

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
        row = self.board[pos.y]
        return Board.__get_subarray_with_distance(row, distance, pos.x)

    def get_col_at(self, pos, distance=0):
        col = [row[pos.x] for row in self.board]
        return Board.__get_subarray_with_distance(col, distance, pos.y)

    def get_principal_diagonal(self, pos, distance=0):
        offset = pos.x - pos.y
        diag = [row[offset + i] for i, row in enumerate(self.board) if 0 <= offset + i < len(row)]
        return Board.__get_subarray_with_distance(diag, distance, min(pos.x, pos.x - offset))

    def get_counter_diagonal(self, pos, distance=0):
        offset = pos.y + pos.x
        diag = [row[offset - i] for i, row in enumerate(self.board) if 0 <= offset - i < len(row)]
        if offset < self.size:
            idx = pos.y
        else:
            idx = pos.y - (offset - (self.size - 1))
        return Board.__get_subarray_with_distance(diag, distance, idx)

    @staticmethod
    def __get_subarray_with_distance(array, distance, i):
        if distance == 0:
            return array
        left_i = max(0, i - distance)
        right_i = min(len(array), i + distance + 1)
        return array[left_i:right_i]

    def get_positions_around(self, pos):
        positions_around = []
        self.__append_if_in(positions_around, Pos(pos.y, pos.x + 1))
        self.__append_if_in(positions_around, Pos(pos.y, pos.x + 2))
        self.__append_if_in(positions_around, Pos(pos.y, pos.x - 1))
        self.__append_if_in(positions_around, Pos(pos.y, pos.x - 2))

        self.__append_if_in(positions_around, Pos(pos.y + 1, pos.x))
        self.__append_if_in(positions_around, Pos(pos.y + 2, pos.x))
        self.__append_if_in(positions_around, Pos(pos.y - 1, pos.x))
        self.__append_if_in(positions_around, Pos(pos.y - 2, pos.x))

        self.__append_if_in(positions_around, Pos(pos.y + 1, pos.x + 1))
        self.__append_if_in(positions_around, Pos(pos.y + 2, pos.x + 1))
        self.__append_if_in(positions_around, Pos(pos.y - 1, pos.x + 1))
        self.__append_if_in(positions_around, Pos(pos.y - 2, pos.x + 1))

        self.__append_if_in(positions_around, Pos(pos.y + 1, pos.x + 2))
        self.__append_if_in(positions_around, Pos(pos.y + 2, pos.x + 2))
        self.__append_if_in(positions_around, Pos(pos.y - 1, pos.x + 2))
        self.__append_if_in(positions_around, Pos(pos.y - 2, pos.x + 2))

        self.__append_if_in(positions_around, Pos(pos.y + 1, pos.x - 1))
        self.__append_if_in(positions_around, Pos(pos.y + 2, pos.x - 1))
        self.__append_if_in(positions_around, Pos(pos.y - 1, pos.x - 1))
        self.__append_if_in(positions_around, Pos(pos.y - 2, pos.x - 1))

        self.__append_if_in(positions_around, Pos(pos.y + 1, pos.x - 2))
        self.__append_if_in(positions_around, Pos(pos.y + 2, pos.x - 2))
        self.__append_if_in(positions_around, Pos(pos.y - 1, pos.x - 2))
        self.__append_if_in(positions_around, Pos(pos.y - 2, pos.x - 2))
        return positions_around

    def __append_if_in(self, array, pos):
        if self.is_in(pos):
            array.append(pos)
