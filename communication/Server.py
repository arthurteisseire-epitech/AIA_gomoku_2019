from sys import stdin
from communication.Dispatcher import Dispatcher
from communication.output import send
from board.Board import Board


class Server:

    @staticmethod
    def start():
        dispatcher = Dispatcher(Board(19))
        for line in stdin:
            response = dispatcher.dispatch(line)
            if response == "end":
                exit(0)
            elif response:
                send(response)
