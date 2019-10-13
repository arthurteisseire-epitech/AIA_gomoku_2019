from random import randrange
from output import send


def start():
    send("OK")


def turn():
    send(str(randrange(19)) + ',' + str(randrange(19)))


def end():
    exit(0)


commands = [
    ["START", start],
    ["RESTART", start],
    ["TURN", turn],
    ["BEGIN", turn],
    ["END", end],
]


def dispatch(line):
    for command in commands:
        if command[0] in line:
            command[1]()
