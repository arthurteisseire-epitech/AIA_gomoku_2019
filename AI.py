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

    @staticmethod
    def evaluation_of_position(board: Board, pos: Pos):
        weight = 0

        if board.get_info_at(pos) != Tile.EMPTY:
            return weight
        for y in range(0, board.size):
            tile = Tile(board.get_info_at(Pos(pos.x, y)))
            if tile == Tile.MINE:
                weight += 1
        return weight
