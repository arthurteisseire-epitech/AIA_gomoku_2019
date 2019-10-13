from Board import Board, Tile
from random import randrange


class AI:
    @staticmethod
    def next_move(board: Board):
        x = randrange(board.size)
        y = randrange(board.size)
        while board.get_info_at(x, y) != Tile.EMPTY:
            x = randrange(board.size)
            y = randrange(board.size)
        return x, y
