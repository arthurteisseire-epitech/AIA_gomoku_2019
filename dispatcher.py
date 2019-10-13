from random import randrange
from output import send, debug


def start(args):
    send("OK")


def turn(args):
    send(str(randrange(19)) + ',' + str(randrange(19)))


def end(args):
    exit(0)


commands = [
    ["START", start],
    ["RESTART", start],
    ["TURN", turn],
    ["BEGIN", turn],
    ["END", end],
]


def dispatch(line):
    tokens = line.strip('\r\n').split(' ')
    for command in commands:
        if command[0] == tokens[0]:
            command[1](tokens[:1])
            break
