import math
from Board import Board, Tile
from Pos import Pos
from Player import Player


class Evaluation:
    LOOSE_GAME = -10
    WIN_GAME = 10
    DRAW = 0
    INFINITE = math.inf

    @staticmethod
    def evaluation_board(board: Board, player: Player):
        my_stones, opponent_stones = Evaluation.get_stones(board, player)
        my_weight = 0

        for pos in my_stones:
            my_weight += Evaluation.calc_weight_for(board.get_row_at(pos, 4), player)
            my_weight += Evaluation.calc_weight_for(board.get_col_at(pos, 4), player)
            my_weight += Evaluation.calc_weight_for(board.get_principal_diagonal(pos, 4), player)
            my_weight += Evaluation.calc_weight_for(board.get_counter_diagonal(pos, 4), player)

        return my_weight

    @staticmethod
    def calc_weight_for(array, player):
        arrlen = len(array)
        if arrlen != 9:
            return 0
        middle_idx = (arrlen - 1) // 2
        weight = Evaluation.calc_weight_for_left(array, middle_idx, player) + Evaluation.calc_weight_for_right(array, middle_idx, player)
        return weight

    @staticmethod
    def calc_weight_for_left(array, middle_idx, player):
        weight = 1
        for i in range(middle_idx - 1, -1, -1):
            tile = array[i]
            if tile == Tile.EMPT:
                break
            if tile == Evaluation.get_opponent_stone(player):
                weight = 0
                break
            weight *= 20
        return weight

    @staticmethod
    def calc_weight_for_right(array, middle_idx, player):
        weight = 1
        for i in range(middle_idx + 1, len(array)):
            tile = array[i]
            if tile == Tile.EMPT:
                break
            if tile == Evaluation.get_opponent_stone(player):
                weight = 0
                break
            weight *= 20
        return weight

    @staticmethod
    def evaluate_stone(tile, player, weight):
        w = 0
        if tile == Tile.EMPT:
            w = weight + 2
        elif tile == Evaluation.get_my_stone(player):
            w = weight * 16
        elif tile == Evaluation.get_opponent_stone(player):
            w = weight * 50
        return w

    @staticmethod
    def get_stones(board, player):
        my_stones = []
        opponent_stones = []
        for y in range(0, board.size):
            for x in range(0, board.size):
                pos = Pos(y, x)
                tile = board.get_info_at(pos)
                if tile == Evaluation.get_my_stone(player):
                    my_stones.append(pos)
                elif tile == Evaluation.get_opponent_stone(player):
                    opponent_stones.append(pos)
        return my_stones, opponent_stones

    @staticmethod
    def get_my_stone(player: Player):
        return Tile.MINE if player == Player.MINE else Tile.OPPO

    @staticmethod
    def get_opponent_stone(player: Player):
        return Tile.MINE if player == Player.OPPONENT else Tile.OPPO

    @staticmethod
    def __count_same_tile_in(array, tile):
        return len(list(filter(lambda x: x == tile, array)))

    @staticmethod
    def is_game_lose(e):
        return e == Evaluation.LOOSE_GAME

    @staticmethod
    def is_game_won(e):
        return e == Evaluation.WIN_GAME
