import math
from Board import Board, Tile
from Pos import Pos

class Weight:

    def __init__(self):
        self.OPPONENT = 2
        self.MINE = 2
        self.DAME = 0
        self.INFINITE = math.inf

    @staticmethod
    def __attribute_weight(my_weight, opponent_weight):
        weight = 0

        if my_weight == 2 and opponent_weight == 0:
            weight = math.inf
        if my_weight == 0 and opponent_weight == 2:
            weight = 10
        if my_weight == 1 and opponent_weight == 0:
            weight = 3
        if my_weight == 0 and opponent_weight == 1:
            weight = 2
        if my_weight == 0 and opponent_weight == 0:
            weight = 1
        return weight
    @staticmethod
    def __count_same_tile_in_row(board: Board, pos: Pos, tile: Tile):
        return len(list(filter(lambda x: x == tile, board.get_row_at(pos))))

    @staticmethod
    def __count_same_tile_in_col(board: Board, pos: Pos, tile: Tile):
        return len(list(filter(lambda x: x == tile, board.get_col_at(pos))))

    @staticmethod
    def __count_same_tile_in_principal_diagonal(board: Board, pos: Pos, tile: Tile):
        return len(list(filter(lambda x: x == tile, board.get_principal_diagonal(pos))))

    @staticmethod
    def __count_same_tile_in_counter_diagonal(board: Board, pos: Pos, tile: Tile):
        return len(list(filter(lambda x: x == tile, board.get_counter_diagonal(pos))))

    @staticmethod
    def __calc_weight_for_row(board: Board, pos: Pos):
        my_weight = Weight.__count_same_tile_in_row(board, pos, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in_row(board, pos, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    @staticmethod
    def __calc_weight_for_col(board: Board, pos: Pos):
        my_weight = Weight.__count_same_tile_in_col(board, pos, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in_col(board, pos, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    @staticmethod
    def __calc_weight_for_principal(board: Board, pos: Pos):
        my_weight = Weight.__count_same_tile_in_principal_diagonal(board, pos, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in_principal_diagonal(board, pos, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    @staticmethod
    def __calc_weight_for_counter(board: Board, pos: Pos):
        my_weight = Weight.__count_same_tile_in_counter_diagonal(board, pos, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in_counter_diagonal(board, pos, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    def evaluation_of_position(self, board: Board, pos: Pos):
        if board.get_info_at(pos) != Tile.EMPTY:
            raise Exception
        weight = Weight.__calc_weight_for_row(board, pos)
        weight += Weight.__calc_weight_for_col(board, pos)
        weight += Weight.__calc_weight_for_principal(board, pos)
        weight += Weight.__calc_weight_for_counter(board, pos)
        return weight
