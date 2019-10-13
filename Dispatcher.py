from Command import Command


class Dispatcher:
    __commands = [
        ["START", Command.start],
        ["RESTART", Command.start],
        ["TURN", Command.turn],
        ["BEGIN", Command.turn],
        ["END", Command.end],
    ]

    @staticmethod
    def dispatch(line):
        tokens = line.strip('\r\n').split(' ')
        for command in Dispatcher.__commands:
            if command[0] == tokens[0]:
                return command[1](tokens[:1])
        return ""
