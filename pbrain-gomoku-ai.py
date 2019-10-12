#!/usr/bin/python3

import sys
from random import randrange


def send(s):
    print(s)
    sys.stdout.flush()


def start():
    send("OK")


def turn():
    send(str(randrange(19)) + ',' + str(randrange(19)))


commands = [
    ["START", start],
    ["TURN", turn],
    ["BEGIN", turn],
]

for line in sys.stdin:
    for command in commands:
        if command[0] in line:
            command[1]()
