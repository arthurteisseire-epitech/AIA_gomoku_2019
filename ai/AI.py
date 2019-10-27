from board.Board import Board, Tile
from board.Pos import Pos
from ai.Evaluation import Evaluation
from ai.find_potential_positions import find_potential_positions
from copy import deepcopy
from ai.Player import Player


class AI:
    @staticmethod
    def next_move(board: Board):
        return AI.find_best_position(board)

    @staticmethod
    def find_best_position(board):
        max_val = -Evaluation.INFINITE
        best_pos = Pos(0, 0)
        potential_positions = find_potential_positions(board)
        for pos in potential_positions:
            if board.get_info_at(pos) == Tile.EMPT:
                new_board = deepcopy(board)
                new_board.set_info_at(pos, Tile.MINE)
                val = Evaluation.evaluation_board(new_board, Player.MINE)
                # val = Algo.minimax(new_board, 1)
                if val > max_val:
                    max_val = val
                    best_pos = pos
        return best_pos
