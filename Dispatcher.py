import re
from AI import AI
from Board import Board, Tile


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
        tokens = list(filter(lambda x: x != '', re.split('[\r\n ]', line)))
        for command in self.__commands:
            if command[0] == tokens[0]:
                return command[1](tokens[1:])
        return ""

    def start(self, args):
        if len(args) == 1 and args[0].isdigit():
            self.board = Board(int(args[0]))
        return "OK"

    def restart(self, *unused):
        self.board = Board(self.board.size)
        return "OK"

    def begin(self, *unused):
        middle = self.board.size // 2 + 1
        self.board.set_info_at(middle, middle, Tile.OPPONENT)
        return str(middle) + ',' + str(middle)

    def turn(self, args):
        if len(args) != 1:
            return ''
        pos = args[0].split(',')
        if len(pos) != 2 or pos[0].isdigit is False or pos[1].isdigit is False:
            return ''
        self.board.set_info_at(int(pos[0]), int(pos[1]), Tile.OPPONENT)
        x, y = AI.next_move(self.board)
        self.board.set_info_at(x, y, Tile.MINE)
        return str(x) + ',' + str(y)

    def about(self, *unused):
        return "name=gomoku-ai, version=1.0, author=boom, country=France"

    def end(self, *unused):
        return "end"
