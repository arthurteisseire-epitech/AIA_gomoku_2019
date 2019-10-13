from random import randrange


class Command:
    @staticmethod
    def start(args):
        return "OK"

    @staticmethod
    def turn(args):
        return str(randrange(19)) + ',' + str(randrange(19))

    @staticmethod
    def end(args):
        return "end"


