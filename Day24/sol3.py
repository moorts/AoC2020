with open('./input2') as f:
    data = f.readlines()

lines = [line.rstrip() for line in data]

directions = {
    'w': (0, -1),
    'e': (0, 1),
    'se': (-0.5, 0.5),
    'ne': (0.5, 0.5),
    'sw': (-0.5, -0.5),
    'nw': (0.5, -0.5)
}

class Tile:
    def __init__(self):
        self.nb = set()
        self.black = False

    def count(self):
        c = 0 
        for tile in self.nb:
            if tile.black:
                c += 1
        return c

