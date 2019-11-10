import math
from Board import Board, Tile
from Pos import Pos
from Player import Player
from itertools import groupby


class Evaluation:
    LOOSE_GAME = -10
    WIN_GAME = 10
    DRAW = 0
    INFINITE = math.inf

    @staticmethod
    def evaluation_board(board: Board, player: Player):
        my_stones, opponent_stones = Evaluation.get_stones(board, player)

        my_weight = Evaluation.calc_weight_for(board, player, my_stones, Evaluation.is_won)
        if my_weight == math.inf:
            return my_weight

        opponent_weight = Evaluation.calc_weight_for(board, Evaluation.get_opponent(player), opponent_stones, Evaluation.can_win)
        if opponent_weight == math.inf:
            return -opponent_weight
        return my_weight

    @staticmethod
    def calc_weight_for(board, player, stones, check_win_func):
        weight = 0
        for pos in stones:
            weight += Evaluation.calc_array_weight_for(board.get_row_at(pos, 4), player, check_win_func)
            weight += Evaluation.calc_array_weight_for(board.get_col_at(pos, 4), player, check_win_func)
            weight += Evaluation.calc_array_weight_for(board.get_principal_diagonal(pos, 4), player, check_win_func)
            weight += Evaluation.calc_array_weight_for(board.get_counter_diagonal(pos, 4), player, check_win_func)
        return weight

    @staticmethod
    def calc_array_weight_for(array, player, check_win_func):
        arrlen = len(array)
        if check_win_func(array, Evaluation.get_my_stone(player)):
            return math.inf
        if arrlen != 9:
            return 0
        middle_idx = (arrlen - 1) // 2
        weight = Evaluation.calc_weight_for_left(array, middle_idx, player) + Evaluation.calc_weight_for_right(array, middle_idx, player)
        return weight

    @staticmethod
    def is_won(array, tile):
        return Evaluation.are_consecutive(array, tile, 5)

    @staticmethod
    def can_win(array, tile):
        is_over = Evaluation.check_empty_then_four_consecutive(array, tile)
        if is_over:
            return True
        rev_array = list(reversed(array))
        is_over = Evaluation.check_empty_then_four_consecutive(rev_array, tile)
        return is_over

    @staticmethod
    def check_empty_then_four_consecutive(array, tile):
        for i in range(len(array)):
            counter = 0
            if array[i] == Tile.EMPT:
                for t in array[i + 1:]:
                    if t != tile:
                        break
                    else:
                        counter += 1
                if counter == 4:
                    return True
        return False

    @staticmethod
    def are_consecutive(array, tile, nb):
        return any(sum(1 for _ in g) >= nb for t, g in groupby(array) if t == tile)

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
    def get_opponent(player: Player):
        return Player.MINE if player == Player.OPPONENT else Player.OPPONENT

    @staticmethod
    def __count_same_tile_in(array, tile):
        return len(list(filter(lambda x: x == tile, array)))

    @staticmethod
    def is_game_lose(e):
        return e == Evaluation.LOOSE_GAME

    @staticmethod
    def is_game_won(e):
        return e == Evaluation.WIN_GAME
