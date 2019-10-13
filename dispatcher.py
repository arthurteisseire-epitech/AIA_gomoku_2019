from command import Command


class Dispatcher:
    def __init__(self):
        self.commands = [
            ["START", Command.start],
            ["RESTART", Command.start],
            ["TURN", Command.turn],
            ["BEGIN", Command.turn],
            ["END", Command.end],
        ]

    def dispatch(self, line):
        tokens = line.strip('\r\n').split(' ')
        for command in self.commands:
            if command[0] == tokens[0]:
                return command[1](tokens[:1])
        return ""
