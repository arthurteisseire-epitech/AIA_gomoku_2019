from Board import Board, Tile
from random import randrange
from Pos import Pos
from Weight import Weight


class AI:
    @staticmethod
    def next_move(board: Board):
        pos = Pos(randrange(board.size), randrange(board.size))
        while board.get_info_at(pos) != Tile.EMPTY:
            pos = Pos(randrange(board.size), randrange(board.size))
        return pos

    @staticmethod
    def find_best_position(board: Board):
        board_weight = []
        for y in range(0, board.size):
            for x in range(0, board.size):
                try:
                    board_weight.append(Weight.evaluation_of_position(board, Pos(y, x)))
                except:
                    board_weight.append(0)
        idx = board_weight.index(max(board_weight))
        return Pos(idx // board.size, idx % board.size)
