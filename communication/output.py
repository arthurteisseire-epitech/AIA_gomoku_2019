def send(s):
    print(s, flush=True)


def debug(s):
    send("DEBUG " + s)
