from random import randrange
from Board import Board


class Dispatcher:
    def __init__(self, board):
        self.board = board

        self.__commands = [
            ["START", self.start],
            ["RESTART", self.start],
            ["TURN", self.turn],
            ["BEGIN", self.turn],
            ["END", self.end],
        ]

    def dispatch(self, line):
        tokens = line.strip('\r\n').split(' ')
        for command in self.__commands:
            if command[0] == tokens[0]:
                return command[1](tokens[1:])
        return ""

    def start(self, args):
        if len(args) == 1 and args[0].isdigit():
            self.board = Board(int(args[0]))
        return "OK"

    def turn(self, args):
        return str(randrange(self.board.size)) + ',' + str(randrange(self.board.size))

    def end(self, args):
        return "end"
