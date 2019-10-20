import re
from AI import AI
from Board import Board, Tile
from Pos import Pos


class Dispatcher:
    def __init__(self, board):
        self.board = board
        self.__commands = [
            ["START", self.start],
            ["RESTART", self.restart],
            ["ABOUT", self.about],
            ["TURN", self.turn],
            ["BEGIN", self.begin],
            ["END", self.end],
        ]

    def dispatch(self, line):
        try:
            return self.safe_dispatch(line)
        except:
            return "DEBUG " + line.strip('\r\n') + ": invalid command."

    def safe_dispatch(self, line):
        tokens = list(filter(lambda x: x != '', re.split('[\r\n ]', line)))
        if not tokens:
            return ""
        for command in self.__commands:
            if command[0] == tokens[0]:
                return command[1](tokens[1:])
        raise

    def start(self, args):
        size = int(args[0])
        if size <= 0:
            raise
        self.board = Board(size)
        return "OK"

    def restart(self, *unused):
        self.board = Board(self.board.size)
        return "OK"

    def begin(self, *unused):
        middle = self.board.size // 2 + 1
        self.board.set_info_at(middle, middle, Tile.OPPONENT)
        return str(middle) + ',' + str(middle)

    def turn(self, args):
        input_pos = args[0].split(',')
        self.board.set_info_at(Pos(int(input_pos[1]), int(input_pos[0])), Tile.OPPONENT)
        pos = AI.next_move(self.board)
        self.board.set_info_at(pos, Tile.MINE)
        return pos.to_string()

    def about(self, *unused):
        return "name=gomoku-ai, version=1.0, author=boom, country=France"

    def end(self, *unused):
        return "end"
