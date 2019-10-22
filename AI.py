from Board import Board
from Pos import *
from Weight import Weight


class AI:
    @staticmethod
    def next_move(board: Board):
        return AI.find_best_positions(board)[0][0]

    @staticmethod
    def find_best_positions(board: Board):
        board_weight = AI.create_board_weight_from_board(board)
        sorted_board_weight = sorted(board_weight, key=lambda elem: elem[1], reverse=True)
        return sorted_board_weight[:5]

    @staticmethod
    def create_board_weight_from_board(board):
        board_weight = []
        for y in range(0, board.size):
            for x in range(0, board.size):
                pos = Pos(y, x)
                weight = Weight.evaluation_of_position(board, pos)
                board_weight.append([pos, weight])
        return board_weight
