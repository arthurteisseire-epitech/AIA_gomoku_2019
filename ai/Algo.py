from ai.Evaluation import Evaluation
from board.Board import Tile
from board.Pos import Pos
from copy import deepcopy


class Algo:
    @staticmethod
    def minimax(board, depth=-1, alpha=-Evaluation.INFINITE, beta=Evaluation.INFINITE, maximizing_player=False):
        e = Evaluation.evaluation_board(board)
        if depth == 0 or Evaluation.is_game_lose(e) or Evaluation.is_game_won(e):
            return e
        if board.is_full():
            return Evaluation.DRAW

        if maximizing_player:
            max_eval = -Evaluation.INFINITE
            for y in range(0, board.size):
                for x in range(0, board.size):
                    tmp_pos = Pos(y, x)
                    if board.get_info_at(tmp_pos) == Tile.EMPTY:
                        new_board = deepcopy(board)
                        new_board.set_info_at(tmp_pos, Tile.MINE)
                        tmp_eval = Algo.minimax(new_board, depth - 1, alpha, beta, False)
                        max_eval = max(tmp_eval, max_eval)
                        alpha = max(alpha, tmp_eval)
                        if beta <= alpha:
                            return max_eval
            return max_eval
        else:
            min_eval = Evaluation.INFINITE
            for y in range(0, board.size):
                for x in range(0, board.size):
                    tmp_pos = Pos(y, x)
                    if board.get_info_at(tmp_pos) == Tile.EMPTY:
                        new_board = deepcopy(board)
                        new_board.set_info_at(tmp_pos, Tile.OPPONENT)
                        tmp_eval = Algo.minimax(new_board, depth - 1, alpha, beta, True)
                        min_eval = min(tmp_eval, min_eval)
                        beta = min(beta, tmp_eval)
                        if beta <= alpha:
                            return min_eval
            return min_eval
