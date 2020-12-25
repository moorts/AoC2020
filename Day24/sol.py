with open('./input') as f:
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

flipped = dict()
for line in lines:
    coords = [0, 0]
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
for k, v in flipped.items():
    if v % 2 != 0:
        count += 1
print(count)


    
