with open('./input') as f:
    data = f.readlines()

lines = [line.rstrip() for line in data]

directions = {
    'w': (0.0, -1.0),
    'e': (0.0, 1.0),
    'se': (-1.0, 0.5),
    'ne': (1.0, 0.5),
    'sw': (-1.0, -0.5),
    'nw': (1.0, -0.5)
}

flipped = dict()
for line in lines:
    coords = [0.0, 0.0]
    i = 0
    while i < len(line):
        if line[i] in directions:
            d = directions[line[i]]
            i += 1
        else:
            d = directions[line[i:i+2]]
            i += 2
        coords[0] += d[0]
        coords[1] += d[1]
    coords = tuple(coords)
    if coords in flipped:
        flipped[coords] += 1
    else:
        flipped[coords] = 1

count = 0
tiles = set()
for k, v in flipped.items():
    if v % 2 != 0:
        count += 1
        tiles.add(k)

print(tiles)
for i in range(100):
    white = set()

    removal = set()
    for tile in tiles:
        bc = 0
        for k, v in directions.items():
            n = (tile[0] + v[0], tile[1] + v[1])
            if n in tiles:
                bc += 1
            else:
                white.add(n)
        if bc == 0 or bc > 2:
            removal.add(tile)

    new_tiles = set()
    for tile in white:
        bc = 0
        for k, v in directions.items():
            n = (tile[0] + v[0], tile[1] + v[1])
            if n in tiles:
                bc += 1
        if bc == 2:
            new_tiles.add(tile)
    for tile in removal:
        tiles.remove(tile)
    for tile in new_tiles:
        tiles.add(tile)
print(len(tiles))


