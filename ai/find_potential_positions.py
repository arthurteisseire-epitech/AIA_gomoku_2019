from board.Board import Tile
from board.Pos import Pos


def find_potential_positions(board):
    best_positions = []
    for y in range(0, board.size):
        for x in range(0, board.size):
            pos = Pos(y, x)
            positions_around = board.get_positions_around(pos)
            if len(list(filter(lambda p: board.get_info_at(p) != Tile.EMPT, positions_around))) > 0:
                best_positions.append(pos)
    return best_positions
