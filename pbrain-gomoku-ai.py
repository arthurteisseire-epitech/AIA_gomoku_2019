#!/usr/bin/python3

from sys import stdin
from Dispatcher import Dispatcher
from output import send


for line in stdin:
    response = Dispatcher.dispatch(line)
    if response == "end":
        exit(0)
    elif response:
        send(response)
