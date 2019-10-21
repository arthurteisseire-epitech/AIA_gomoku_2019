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
        weight_mine_in_row = len(list(filter(lambda x: x == Tile.MINE, board.get_row_at(pos)))) * Weight.MINE
        weight_mine_in_col = len(list(filter(lambda x: x == Tile.MINE, board.get_col_at(pos)))) * Weight.MINE
        weight_opponent_in_row = len(
            list(filter(lambda x: x == Tile.OPPONENT, board.get_row_at(pos)))) * Weight.OPPONENT
        weight_opponent_in_col = len(
            list(filter(lambda x: x == Tile.OPPONENT, board.get_col_at(pos)))) * Weight.OPPONENT
        weight_mine_top_left_to_bottom_right = len(
            list(filter(lambda x: x == Tile.MINE, board.get_diagonal_top_left_to_bottom_right(pos)))) * Weight.MINE
        weight_mine_top_right_to_bottom_left = len(
            list(filter(lambda x: x == Tile.MINE, board.get_diagonal_top_right_to_bottom_left(pos)))) * Weight.MINE
        weight_opponent_top_left_to_bottom_right = len(list(
            filter(lambda x: x == Tile.OPPONENT, board.get_diagonal_top_left_to_bottom_right(pos)))) * Weight.OPPONENT
        weight_opponent_top_right_to_bottom_left = len(list(
            filter(lambda x: x == Tile.OPPONENT, board.get_diagonal_top_right_to_bottom_left(pos)))) * Weight.OPPONENT
        return weight_mine_in_row + weight_mine_in_col + weight_opponent_in_row + weight_opponent_in_col + \
               weight_mine_top_left_to_bottom_right + weight_mine_top_right_to_bottom_left + \
               weight_opponent_top_left_to_bottom_right + weight_opponent_top_right_to_bottom_left
