import re
import sys
from AI import AI
from Board import Board, Tile
from Pos import Pos
from output import debug


class Dispatcher:
    def __init__(self, board):
        self.board = board
        self.__commands = [
            ["START", self.start],
            ["RESTART", self.restart],
            ["BOARD", self.reset_board],
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

    def reset_board(self, *unused):
        self.board = Board(self.board.size)
        for line in sys.stdin:
            line = line.rstrip('\r\n')
            if line == "DONE":
                return self.ai_play()
            else:
                tokens = line.split(',')
                success = self.board.set_info_at(Pos(int(tokens[1]), int(tokens[0])), Tile(int(tokens[2])))
                if not success:
                    raise
        raise

    def begin(self, *unused):
        middle = self.board.size // 2 + 1
        pos = Pos(middle, middle)
        self.board.set_info_at(pos, Tile.OPPONENT)
        return pos.to_string()

    def turn(self, args):
        input_pos = args[0].split(',')
        self.board.set_info_at(Pos(int(input_pos[1]), int(input_pos[0])), Tile.OPPONENT)
        return self.ai_play()

    def about(self, *unused):
        return "name=gomoku-ai, version=1.0, author=boom, country=France"

    def end(self, *unused):
        return "end"

    def ai_play(self):
        pos = AI.next_move(self.board)
        self.board.set_info_at(pos, Tile.MINE)
        return pos.to_string()
