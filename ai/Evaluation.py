import math
import env
from board.Board import Board, Tile
from board.Pos import Pos


class Evaluation:
    LOOSE_GAME = -10
    WIN_GAME = 10
    DRAW = 0
    INFINITE = math.inf

    @staticmethod
    def evaluation_board(board: Board):
        for i in range(0, env.STONES_TO_WIN):
            val = Evaluation.__calc_val_for(board.get_row_at(Pos(i, 0)))
            if val != 0:
                return val

        for i in range(0, env.STONES_TO_WIN):
            val = Evaluation.__calc_val_for(board.get_col_at(Pos(0, i)))
            if val != 0:
                return val

        val = Evaluation.__calc_val_for(board.get_principal_diagonal(Pos(0, 0)))
        if val != 0:
            return val

        val = Evaluation.__calc_val_for(board.get_counter_diagonal(Pos(0, 2)))
        if val != 0:
            return val

        return 0

    @staticmethod
    def __calc_val_for(array):
        my_consecutive_tiles = Evaluation.__count_same_tile_in(array, Tile.MINE)
        if my_consecutive_tiles == env.STONES_TO_WIN:
            return Evaluation.WIN_GAME
        opponent_consecutive_tiles = Evaluation.__count_same_tile_in(array, Tile.OPPONENT)
        if opponent_consecutive_tiles == env.STONES_TO_WIN:
            return Evaluation.LOOSE_GAME
        return 0

    @staticmethod
    def __count_same_tile_in(array, tile):
        return len(list(filter(lambda x: x == tile, array)))

    @staticmethod
    def is_game_lose(e):
        return e == Evaluation.LOOSE_GAME

    @staticmethod
    def is_game_won(e):
        return e == Evaluation.WIN_GAME
