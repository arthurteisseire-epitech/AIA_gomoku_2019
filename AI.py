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
    def evaluation_of_position(board: Board, pos: Pos):
        if board.get_info_at(pos) != Tile.EMPTY:
            raise Exception
        weight_opponent = AI.calc_weight_for(board, pos, Tile.OPPONENT, Weight.OPPONENT)
        weight_mine = AI.calc_weight_for(board, pos, Tile.MINE, Weight.MINE)
        return weight_opponent + weight_mine

    @staticmethod
    def calc_weight_for(board, pos, tile, weight):
        weight_in_row = len(list(filter(lambda x: x == tile, board.get_row_at(pos)))) * weight
        weight_in_col = len(list(filter(lambda x: x == tile, board.get_col_at(pos)))) * weight
        weight_principal_diagonal = len(list(filter(lambda x: x == tile, board.get_principal_diagonal(pos)))) * weight
        weight_counter_diagonal = len(list(filter(lambda x: x == tile, board.get_counter_diagonal(pos)))) * weight
        return weight_in_col + weight_in_row + weight_principal_diagonal + weight_counter_diagonal
