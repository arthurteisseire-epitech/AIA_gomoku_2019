from Board import Board
from Pos import Pos
from Weight import Weight


class AI:
    @staticmethod
    def next_move(board: Board):
        return AI.find_best_position(board)

    @staticmethod
    def find_best_position(board: Board):
        board_weight = []
        for y in range(0, board.size):
            for x in range(0, board.size):
                board_weight.append(Weight.evaluation_of_position(board, Pos(y, x)))
        idx = board_weight.index(max(board_weight))
        return Pos(idx // board.size, idx % board.size)
