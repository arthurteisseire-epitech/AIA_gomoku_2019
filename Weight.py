import math
import env
from Board import Board, Tile
from Pos import Pos


class Weight:
    LOOSE_GAME = -10
    WIN_GAME = 10
    INFINITE = math.inf

    @staticmethod
    def evaluation_of_position(board: Board):
        for i in range(0, env.STONES_TO_WIN):
            weight = Weight.__calc_weight_for(board.get_row_at(Pos(i, 0)))
            if weight > 0:
                return 10
            elif weight < 0:
                return -10

        for i in range(0, env.STONES_TO_WIN):
            weight = Weight.__calc_weight_for(board.get_col_at(Pos(0, i)))
            if weight > 0:
                return 10
            elif weight < 0:
                return -10

        weight = Weight.__calc_weight_for(board.get_principal_diagonal(Pos(0, 0)))
        if weight > 0:
            return 10
        elif weight < 0:
            return -10

        weight = Weight.__calc_weight_for(board.get_counter_diagonal(Pos(0, 2)))
        if weight > 0:
            return 10
        elif weight < 0:
            return -10

        return 0

    @staticmethod
    def __calc_weight_for(array):
        # if len(array) < env.STONES_TO_WIN:
        #     return 0

        my_nb_tiles = Weight.__count_same_tile_in(array, Tile.MINE)
        if my_nb_tiles == 3:
            return Weight.WIN_GAME
        opponent_nb_tiles = Weight.__count_same_tile_in(array, Tile.OPPONENT)
        if opponent_nb_tiles == 3:
            return Weight.LOOSE_GAME
        return 0

    @staticmethod
    def __count_same_tile_in(array, tile):
        return len(list(filter(lambda x: x == tile, array)))
    #
    # @staticmethod
    # def __attribute_weight(my_weight, opponent_weight):
    #     weights = [
    #         Weight.__win_game(my_weight, opponent_weight),
    #         Weight.__lose_game(my_weight, opponent_weight),
    #     ]
    #     return max(weights)
    #
    # @staticmethod
    # def __win_game(my_weight, opponent_weight):
    #     if my_weight == 3:
    #         return Weight.WIN_GAME
    #     return 0
    #
    # @staticmethod
    # def __lose_game(my_weight, opponent_weight):
    #     if opponent_weight == 3:
    #         return Weight.LOOSE_GAME
    #     return 0
    #
