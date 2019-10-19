class Pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def to_string(self):
        return str(self.x) + ' ' + str(self.y)
