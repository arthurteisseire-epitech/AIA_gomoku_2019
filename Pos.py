class Pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def to_string(self):
        return str(self.x) + ',' + str(self.y)
