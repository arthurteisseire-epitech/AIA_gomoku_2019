from Weight import Weight
from Board import *
from Pos import *
from copy import deepcopy


class Algo:
    @staticmethod
    def minimax(board, find_best_positions_func, depth, maximizing_player=True):
        positions = find_best_positions_func(board)
        if len(positions) == 1:
            return positions[0]
        if depth == 0:
            return positions[0] if maximizing_player else positions[-1]

        if maximizing_player:
            max_pos = WeightBoardPosition(Pos(0, 0), -Weight.INFINITE)
            for pos in positions:
                if board.get_info_at(pos.pos) == Tile.EMPTY:
                    new_board = deepcopy(board)
                    new_board.set_info_at(pos.pos, Tile.MINE)
                    tmp_pos = Algo.minimax(new_board, find_best_positions_func, depth - 1, False)
                    max_pos = tmp_pos if tmp_pos.weight > max_pos.weight else max_pos
            return max_pos
        else:
            min_pos = WeightBoardPosition(Pos(0, 0), Weight.INFINITE)
            for pos in positions:
                if board.get_info_at(pos.pos) == Tile.EMPTY:
                    new_board = deepcopy(board)
                    new_board.set_info_at(pos.pos, Tile.OPPONENT)
                    tmp_pos = Algo.minimax(new_board, find_best_positions_func, depth - 1, True)
                    min_pos = tmp_pos if tmp_pos.weight < min_pos.weight else min_pos
            return min_pos
