
with open('./input2') as f:
    data = f.read()

from parse import *

data = data.split("\n\n")
tiles = [tile.split(":\n") for tile in data]
tiles = [[parse('Tile {:d}', tile[0])[0], tile[1].split("\n")] for tile in tiles]
tiles[len(tiles)-1][1] = tiles[len(tiles)-1][1][:-1]

tiles_dict = dict()
for tile in tiles:
    tiles_dict[tile[0]] = tile[1]


# initial, flipped-horizontal, flipped-vertical, rotated, 
from math import sqrt

dim = int(sqrt(len(tiles)))

ids = [[-1 for i in range(dim)] for j in range(dim)]

def get_mutations(tile):
    mutations = []
    mutations.append(tile[1])
    flipped_h = tile[1][::-1]
    flipped_v = [tile[1][i][::-1] for i in range(len(tile[1]))]
    r1 = flipped_v[::-1]
    r2 = rotate_right(tile)
    r3 = rotate_left(tile)
    mutations.append(flipped_v)
    mutations.append(flipped_h)
    mutations.append(r1)
    mutations.append(r2)
    mutations.append(r3)
    return mutations

def rotate_right(tile):
    rotated = ["".join([tile[1][i][len(tile[1])-j-1] for i in range(len(tile[1]))]) for j in range(len(tile[1]))]
    return rotated

def rotate_left(tile):
    return ["".join([tile[1][len(tile[1])-i-1][j] for i in range(len(tile[1]))]) for j in range(len(tile[1]))]
def get_edges(tile):
    top = tile[1][0]
    bottom = tile[1][len(tile[1])-1]
    right = "".join([tile[1][i][len(tile[1])-1] for i in range(len(tile[1]))])
    left = "".join([tile[1][i][0] for i in range(len(tile[1]))])
    return [top, bottom, left, right]

matches = dict()
for tile in tiles:
    edges = get_edges(tile)
    matches[tile[0]] = []
    for other_tile in tiles:
        if tile[0] == other_tile[0]:
            continue

        other_edges = get_edges(other_tile)

        match = []

        for edge in edges:
            if edge in other_edges:
                idx = edges.index(edge)
                other_idx = other_edges.index(edge)
                match = [idx, other_tile[0], other_idx, False]
            elif edge[::-1] in other_edges:
                idx = edges.index(edge)
                other_idx = other_edges.index(edge[::-1])
                match = [idx, other_tile[0], other_idx, True]

        if len(match) > 0:
            matches[tile[0]].append(match)

squares = [['-' for i in range(dim)] for j in range(dim)]
print(squares)

def calculate_grid(k, m):
    s = [['-' for i in range(dim)] for j in range(dim)]
    start = m[k]
    #s[0][0] = (k, False, False, False, False, False)
    horizontal = False
    vertical = False
    flipped_h = False
    flipped_v = False
    next_v = []
    next_h = []
    for v in m[k]:
        if v[0] < 2:
            if v[0] == 0:
                horizontal = True
            flipped_h = v[3]
            next_h = v
        else:
            if v[0] == 3:
                vertical = True
            flipped_v = v[3]
            next_v = v
    # Calculate next pos
    #print(f"Next right square to {k}: {next_v}, will be flipped: {horizontal or flipped_v}")
    print(f"Next bottom square to {k}: {next_h}, will be flipped: {vertical or flipped_h}")



for k, v in matches.items():
    if len(v) == 2:
        calculate_grid(k, matches)





