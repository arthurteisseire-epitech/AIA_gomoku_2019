#!/usr/bin/python3

from sys import stdin
from Dispatcher import Dispatcher
from output import send
from Board import Board


dispatcher = Dispatcher(Board(19))

for line in stdin:
    response = dispatcher.dispatch(line)
    if response == "end":
        exit(0)
    elif response:
        send(response)
