import math
import env
from Board import Board, Tile
from Pos import Pos


class Weight:
    LOOSE_GAME = 10
    OPPONENT = 6
    MINE = 3
    DAME = 1
    INFINITE = math.inf

    @staticmethod
    def evaluation_of_position(board: Board, pos: Pos):
        # if board.get_info_at(pos) != Tile.EMPTY:
        #     return 0
        # instead of adding we should compare weights
        weight = Weight.__calc_weight_for(board.get_row_at(pos))
        weight += Weight.__calc_weight_for(board.get_col_at(pos))
        weight += Weight.__calc_weight_for(board.get_principal_diagonal(pos))
        weight += Weight.__calc_weight_for(board.get_counter_diagonal(pos))
        return weight

    @staticmethod
    def __calc_weight_for(array):
        if len(array) < env.STONES_TO_WIN:
            return 0
        my_weight = Weight.__count_same_tile_in(array, Tile.MINE)
        opponent_weight = Weight.__count_same_tile_in(array, Tile.OPPONENT)
        return Weight.__attribute_weight(my_weight, opponent_weight)

    @staticmethod
    def __count_same_tile_in(array, tile):
        return len(list(filter(lambda x: x == tile, array)))

    @staticmethod
    def __attribute_weight(my_weight, opponent_weight):
        weights = [
            Weight.__win_game(my_weight, opponent_weight),
            Weight.__lose_game(my_weight, opponent_weight),
            Weight.__threat_to_win(my_weight, opponent_weight),
            Weight.__threat_to_lose(my_weight, opponent_weight),
            Weight.__neutral_zone(my_weight, opponent_weight)
        ]
        return max(weights)

    @staticmethod
    def __win_game(my_weight, opponent_weight):
        if my_weight == 2 and opponent_weight == 0:
            return Weight.INFINITE
        return 0

    @staticmethod
    def __lose_game(my_weight, opponent_weight):
        if my_weight == 0 and opponent_weight == 2:
            return Weight.LOOSE_GAME
        return 0

    @staticmethod
    def __threat_to_win(my_weight, opponent_weight):
        if my_weight == 1 and opponent_weight == 0:
            return Weight.MINE
        return 0

    @staticmethod
    def __threat_to_lose(my_weight, opponent_weight):
        if my_weight == 0 and opponent_weight == 1:
            return Weight.OPPONENT
        return 0

    @staticmethod
    def __neutral_zone(my_weight, opponent_weight):
        if my_weight == 0 and opponent_weight == 0:
            return Weight.DAME
        return 0
