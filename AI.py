from Board import Board
from Pos import *
from Weight import Weight
from Algo import Algo
from copy import deepcopy


class AI:
    @staticmethod
    def next_move(board: Board):
        return Algo.minimax(deepcopy(board), AI.find_best_positions, 3).pos

    @staticmethod
    def find_best_positions(board: Board):
        board_weight = AI.create_board_weight_from_board(board)
        sorted_board_weight = sorted(board_weight, key=lambda elem: elem.weight, reverse=True)
        sorted_board_weight = list(filter(lambda elem: elem.weight != 0, sorted_board_weight))
        return sorted_board_weight[:5]

    @staticmethod
    def create_board_weight_from_board(board):
        board_weight = []
        for y in range(0, board.size):
            for x in range(0, board.size):
                pos = Pos(y, x)
                weight = Weight.evaluation_of_position(board, pos)
                board_weight.append(WeightBoardPosition(pos, weight))
        return board_weight
