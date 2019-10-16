from Board import Board, Tile
from random import randrange
from Pos import Pos


class AI:
    @staticmethod
    def next_move(board: Board):
        pos = Pos(randrange(board.size), randrange(board.size))
        while board.get_info_at(pos) != Tile.EMPTY:
            pos = Pos(randrange(board.size), randrange(board.size))
        return pos
