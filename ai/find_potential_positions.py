from board.Board import Board, Tile
from board.Pos import Pos
from ai.Evaluation import Evaluation
from ai.Player import Player
from copy import deepcopy


def find_potential_positions(board):
    best_positions = []
    for y in range(0, board.size):
        for x in range(0, board.size):
            pos = Pos(y, x)
            if board.get_info_at(pos) == Tile.EMPT:
                new_board = deepcopy(board)
                new_board.set_info_at(pos, Tile.MINE)
                best_positions.append([Evaluation.evaluation_board(new_board, Player.MINE), pos])
    sorted_positions = sorted(best_positions, key=lambda elem: elem[0], reverse=True)[:5]
    return list(map(lambda elem: elem[1], sorted_positions))
