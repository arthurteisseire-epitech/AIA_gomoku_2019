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
    def find_best_position(board: Board):
        board_weight = AI.create_board_weight_from_board(board)
        idx = board_weight.index(max(board_weight))
        return Pos(idx // board.size, idx % board.size)

    @staticmethod
    def create_board_weight_from_board(board):
        board_weight = []
        for y in range(0, board.size):
            for x in range(0, board.size):
                pos = Pos(y, x)
                # weight = Weight.evaluation_of_position(board, pos)
                weight = 0
                if board.get_info_at(pos) == Tile.EMPTY:
                    weight = Algo.minimax(board, pos, Weight.evaluation_of_position, 3)
                board_weight.append(weight)
        return board_weight
