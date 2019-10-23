from sys import stdout


def send(s):
    print(s)
    stdout.flush()


def debug(s):
    send("DEBUG " + s)
