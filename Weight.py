import math
from Board import Board, Tile
from Pos import Pos


class Weight:
    OPPONENT = 2
    MINE = 2
    DAME = 0
    INFINITE = math.inf

    @staticmethod
    def __win_game(my_weight, opponent_weight):
        if my_weight == 2 and opponent_weight == 0:
            return math.inf
        return -1

    @staticmethod
    def __lose_game(my_weight, opponent_weight):
        if my_weight == 0 and opponent_weight == 2:
            return 10
        return -1

    @staticmethod
    def __threat_to_win(my_weight, opponent_weight):
        if my_weight == 1 and opponent_weight == 0:
            return 3
        return -1

    @staticmethod
    def __threat_to_lose(my_weight, opponent_weight):
        if my_weight == 0 and opponent_weight == 1:
            return 2
        return -1

    @staticmethod
    def __neutral_zone(my_weight, opponent_weight):
        if my_weight == 0 and opponent_weight == 0:
            return 1
        return -1

    @staticmethod
    def __attribute_weight(my_weight, opponent_weight):
        weights = []

        weights.append(Weight.__win_game(my_weight, opponent_weight))
        weights.append(Weight.__lose_game(my_weight, opponent_weight))
        weights.append(Weight.__threat_to_win(my_weight, opponent_weight))
        weights.append(Weight.__threat_to_lose(my_weight, opponent_weight))
        weights.append(Weight.__neutral_zone(my_weight, opponent_weight))
        return max(weights)

    @staticmethod
    def __calc_weight_for_row(board: Board, pos: Pos):
        row = board.get_row_at(pos)
        my_weight = Weight.__count_same_tile_in(row, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in(row, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    @staticmethod
    def __calc_weight_for_col(board: Board, pos: Pos):
        col = board.get_col_at(pos)
        my_weight = Weight.__count_same_tile_in(col, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in(col, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    @staticmethod
    def __calc_weight_for_principal(board: Board, pos: Pos):
        principal_diagonal = board.get_principal_diagonal(pos)
        my_weight = Weight.__count_same_tile_in(principal_diagonal, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in(principal_diagonal, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    @staticmethod
    def __calc_weight_for_counter(board: Board, pos: Pos):
        counter_diagonal = board.get_counter_diagonal(pos)
        my_weight = Weight.__count_same_tile_in(counter_diagonal, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in(counter_diagonal, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    @staticmethod
    def evaluation_of_position(board: Board, pos: Pos):
        if board.get_info_at(pos) != Tile.EMPTY:
            raise Exception
        # instead of adding we should compare weights
        weight = Weight.__calc_weight_for_row(board, pos)
        weight += Weight.__calc_weight_for_col(board, pos)
        weight += Weight.__calc_weight_for_principal(board, pos)
        weight += Weight.__calc_weight_for_counter(board, pos)
        return weight

    @staticmethod
    def __count_same_tile_in(array, tile):
        return len(list(filter(lambda x: x == tile, array)))
