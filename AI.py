from Board import Board, Tile
from Pos import *
from Weight import Weight
from Algo import Algo
from copy import deepcopy


class AI:
    @staticmethod
    def next_move(board: Board):
        return AI.find_best_position(board)

    @staticmethod
    def find_best_position(board):
        max_val = -Weight.INFINITE
        best_pos = Pos(0, 0)
        for y in range(0, board.size):
            for x in range(0, board.size):
                pos = Pos(y, x)
                weight = -Weight.INFINITE
                if board.get_info_at(pos) == Tile.EMPTY:
                    new_board = deepcopy(board)
                    new_board.set_info_at(pos, Tile.MINE)
                    weight = Algo.minimax(new_board, Weight.evaluation_of_position, 5)
                if weight > max_val:
                    max_val = weight
                    best_pos = pos
        return best_pos
