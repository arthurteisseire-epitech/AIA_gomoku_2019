from Weight import Weight
from Board import *
from Pos import *
from copy import deepcopy


class Algo:
    @staticmethod
    def minimax(board, evaluation_function, depth, maximizing_player=False):
        e = evaluation_function(board)
        if e == Weight.LOOSE_GAME or e == Weight.WIN_GAME:
            return e
        if board.is_full():
            return 0

        if maximizing_player:
            max_eval = -Weight.INFINITE
            for y in range(0, board.size):
                for x in range(0, board.size):
                    tmp_pos = Pos(y, x)
                    if board.get_info_at(tmp_pos) == Tile.EMPTY:
                        new_board = deepcopy(board)
                        new_board.set_info_at(tmp_pos, Tile.MINE)
                        tmp_eval = Algo.minimax(new_board, evaluation_function, depth - 1, False)
                        max_eval = max(tmp_eval, max_eval)
            return max_eval
        else:
            min_eval = Weight.INFINITE
            for y in range(0, board.size):
                for x in range(0, board.size):
                    tmp_pos = Pos(y, x)
                    if board.get_info_at(tmp_pos) == Tile.EMPTY:
                        new_board = deepcopy(board)
                        new_board.set_info_at(tmp_pos, Tile.OPPONENT)
                        tmp_eval = Algo.minimax(new_board, evaluation_function, depth - 1, True)
                        min_eval = min(tmp_eval, min_eval)
            return min_eval
