

with open('./input') as f:
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

class Square:
    def __init__(self, tile):
        self.id = tile[0]
        self.data = tile[1]
        self.size = len(self.data)

    def create(self, data):
        self.data = data

    def right(self):
        return "".join([self.data[i][self.size-1] for i in range(self.size)])
    def left(self):
        return "".join([self.data[i][self.size-1] for i in range(self.size)])
    def top(self):
        return self.data[0]
    def bot(self):
        return self.data[self.size-1]

    def rotate_right(self):
        return Square([self.id, ["".join([self.data[i][len(self.data[1])-j-1] for i in range(len(self.data))]) for j in range(len(self.data))]])

    def rotate_left(self):
        return Square([self.id, ["".join([self.data[len(self.data[1])-i-1][j] for i in range(len(self.data))]) for j in range(len(self.data))]])

    def flip_v(self):
        return Square([self.id, [self.data[i][::-1] for i in range(self.size)]])

    def flip_h(self):
        return Square([self.id, self.data[::-1]])

    def mutations(self):
        m = []
        m.append(self)
        m.append(self.rotate_right())
        m.append(self.rotate_left())
        m.append(self.flip_v())
        m.append(self.flip_h())
        m.append(self.flip_h().flip_v())
        m.append(self.rotate_right().flip_v())
        m.append(self.rotate_left().flip_v())
        return m

    def matches(self, square):
        if self.data[0] == square.data[square.size-1]:
            return 't'
        if self.data[self.size-1] == square.data[0]:
            return 'b'
        if self.col(0) == square.col(square.size-1):
            return 'l'
        if self.col(self.size-1) == square.col(0):
            return 'r'
        return 'x'

    def row(self, row):
        return self.data[row]

    def col(self, col):
        return [self.data[i][col] for i in range(self.size)]

    def __str__(self):
        out = ""
        for row in self.data:
            out += row + "\n"
        return out

class Image:
    def __init__(self, dim: int):
        self.im = [['-' for i in range(dim)] for j in range(dim)]
        self.dim = dim
    def __init__(self, squares):
        self.im = [Square(tile) for tile in squares]
        self.dim = len(self.im)

    def create(self, grid):
        self.im = grid
        self.dim = len(self.im)
    def valid(self):
        pass

    def __getitem__(self, key):
        return self.im[key]

    def print(self):
        print(self.im[0])
        print(self.im[0].size)
        for i in range(dim):
            for x in range(self.im[0].size):
                rows = ""
                for j in range(dim):
                    rows += self.im[i*dim + j].row(x) + "  "
                print(rows)
            print("\n")



image = Image(tiles)
#for tile in tiles:
s = Square(tiles[0])
a = """
...#.##..#
#.#.###.##
....##.#.#
....#...#.
#.##.##...
.##.#....#
#..##.#..#
#..#...###
.#.####.#.
.#####..#.
"""


allowed = dict()
for i in image:
    allowed[i.id] = i.mutations()

match_dict = dict()
match_list = []
for i in image:
    muts = allowed[i.id]
    matches = set()
    for j in image:
        if i.id == j.id:
            continue
        for mi in muts:
            for mj in allowed[j.id]:
                side = mi.matches(mj)
                if side != 'x':
                    matches.add(j.id)
        


    match_dict[i.id] = [i, list(matches)]
    match_list.append([i.id, list(matches), i])


p = []

from itertools import permutations

def dfs(l, last_ids, invalid):
    out = []
    for elem in l[1]:
        if l[0] not in last_ids and elem[1] != invalid:
            if elem[1] == 'r':
                side = 'l'
            elif elem[1] == 'l':
                side = 'r'
            elif elem[1] == 't':
                side = 'b'
            elif elem[1] == 'b':
                side = 't'
            else:
                side = 'x'
            out.append(dfs([elem[0], match_dict[elem[0]]], last_ids + [l[0]], side))
    return [l[0], out]
#print(dfs(match_list[0], [], 'x'))

start = []
for match in match_list:
    if len(match[1]) == 2:
        start.append([match[0], 0, 0])
        break

# Start is top-left
grid = [['-' for i in range(dim)] for j in range(dim)]
grid[0][0] = match_dict[start[0][0]][0]
neighbours = match_dict[start[0][0]][1]
for mut in grid[0][0].mutations():
    rfound = False
    bfound = False
    ridx = None
    bidx = None
    for nmut in match_dict[neighbours[0]][0].mutations():
        if mut.matches(nmut) == 'r':
            rfound = True
            ridx = nmut
        if mut.matches(nmut) == 'b':
            bfound = True
            bidx = nmut
    for lmut in match_dict[neighbours[1]][0].mutations():
        if mut.matches(lmut) == 'r':
            rfound = True
            ridx = lmut
        if mut.matches(lmut) == 'b':
            bfound = True
            bidx = lmut
    if bfound and rfound:
        grid[0][0] = mut
        grid[1][0] = bidx
        grid[0][1] = ridx
        break
#start.pop(0)
#start.append([grid[1][0].id, 0, 1])
#start.append([grid[0][1].id, 1, 0])

print(grid[0][0])
print(grid[1][0])
print(grid[0][1])
x = 1
y = 0
count = 0

def rotate_to_fit(sq1, sq2, side):
    for mut in sq2.mutations():
        if sq1.matches(mut) == side:
            return mut

last = grid[0][1].id
next_row = grid[1][0].id
visited = [grid[0][0].id]
#dim = 1
while True:
    if x == dim-1:
        if y == dim-1:
            break
        y += 1
        x = 0
        last = next_row
    neighbours = match_dict[last][1]
    for n in neighbours:
        print(n)
        print(y,x)
        print(visited)
        if n in visited:
            continue
        for mut in match_dict[n][0].mutations():
            side = grid[y][x].matches(mut)
            if n == 3079:
                print(mut)
                print(grid[y][x])
                print(side)
            if side == 'r':
                visited.append(n)
                grid[y][x+1] = mut
                last = n
            elif x == 0 and side == 'b':
                visited.append(n)
                grid[y+1][x] = mut
                next_row = n
    x += 1

#print(rotate_to_fit(image[1], image[0], 'r'))


l = []
for row in grid:
    l += row

#l = [square.flip_h() for square in l]

print(l)
im = Image([])
im.create(l)
im.print()

def remove_border(square):
    new_square = [['-' for i in range(square.size-2)] for j in range(square.size-2)]
    for i in range(square.size-2):
        for j in range(square.size-2):
            new_square[i][j] = square.data[i+1][j+1]
    return ["".join(line) for line in new_square]

def create_square(data):
    out = Square(tiles[0])
    out.create(data)
    return out

new_squares = [remove_border(sq) for sq in im.im]
print(new_squares)
big_square = []
for i in range(dim):
    for j in range(len(new_squares[0])):
        row = ""
        for k in range(dim):
            row += new_squares[i*dim + k][j]
        big_square.append(row)

big_square = create_square(big_square)
a = "xxxxxxxxxxxxxxxxxx#x"
b = "#xxxx##xxxx##xxxx###"
c = "x#xx#xx#xx#xx#xx#xxx"
monster = [a,b,c]
t1 = "..................#.."
t2 = "#....##....##....###"
t3 = ".#..#..#..#..#..#"
test = [t1, t2, t3]
print(monster[0][0])
def check(mtx, starty, startx, monster_squares):
    found = True
    for i in range(3):
        for j in range(len(monster[0])):
            char = monster[i][j]
            if char == 'x':
                continue
            if mtx[starty+i][startx+j] != char:
                return False
            if mtx[starty+i][startx+j] == '#':
                monster_squares.add((starty+i, startx+j))
    return True

monster_sqs = set()
count = 0
big_square.size = len(big_square.data[0])
print(big_square.size)
mut = None
for sq in big_square.mutations():
    print(sq)
    for i in range(sq.size-2):
        for j in range(sq.size-len(monster[0])):
            temp_sqs = set()
            if check(sq.data, i, j, temp_sqs):
                for squos in temp_sqs:
                    monster_sqs.add(squos)
                count += 1
    if count > 0:
        mut = sq
        break

print(count)
print(len(monster_sqs))
free = 0
for i in range(mut.size):
    for j in range(mut.size):
        if (i, j) not in monster_sqs and mut.data[i][j] == '#':
            free += 1

print(free)

            
