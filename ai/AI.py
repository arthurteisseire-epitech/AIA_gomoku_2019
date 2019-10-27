from board.Board import Board, Tile
from board.Pos import Pos
from ai.Evaluation import Evaluation
from ai.Algo import Algo
from copy import deepcopy


class AI:
    @staticmethod
    def next_move(board: Board):
        return AI.find_best_position(board)

    @staticmethod
    def find_best_position(board):
        max_val = -Evaluation.INFINITE
        best_pos = Pos(0, 0)
        for y in range(0, board.size):
            for x in range(0, board.size):
                pos = Pos(y, x)
                val = -Evaluation.INFINITE
                if board.get_info_at(pos) == Tile.EMPT:
                    new_board = deepcopy(board)
                    new_board.set_info_at(pos, Tile.MINE)
                    val = Algo.minimax(new_board, 3)
                if val > max_val:
                    max_val = val
                    best_pos = pos
        return best_pos
