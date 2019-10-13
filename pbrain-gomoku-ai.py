#!/usr/bin/python3

from sys import stdin
from dispatcher import Dispatcher
from output import send

dispatcher = Dispatcher()

for line in stdin:
    response = dispatcher.dispatch(line)
    if response == "end":
        exit(0)
    elif response:
        send(response)
