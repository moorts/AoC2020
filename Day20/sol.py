with open('./input2') as f:
    data = f.read()

from parse import *

data = data.split("\n\n")
tiles = [tile.split(":\n") for tile in data]
tiles = [[parse('Tile {:d}', tile[0])[0], tile[1].split("\n")] for tile in tiles]
tiles[len(tiles)-1][1] = tiles[len(tiles)-1][1][:-1]


# initial, flipped-horizontal, flipped-vertical, rotated, 
from math import sqrt

dim = int(sqrt(len(tiles)))

ids = [[-1 for i in range(dim)] for j in range(dim)]

def get_mutations(tile):
    mutations = []
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

comp = dict()

adjacent = []
for tile in tiles:
    muts = get_mutations(tile)
    a = [tile[0], []]
    for compare in tiles:
        if tile[0]  == compare[0]:
            continue

        #if compare[0] in comp:
        #    m = [comp[compare[0]]]
        #else:
        m = get_mutations(compare)
        side = ""
        matches = []
        for t in muts:
            done = False
            for x in m:

                if t[0] == x[len(x)-1]:
                    done = True
                    side = "t"
                    new_square = [['-' for i in range(dim)] for j in range(dim)]
                elif t[len(t)-1] == x[0]:
                    done = True
                    side = "b"
                elif [t[i][len(t)-1] for i in range(len(t))] == [x[i][0] for i in range(len(x))]:
                    done = True
                    side = "r"
                elif [t[i][0] for i in range(len(t))] == [x[i][len(x)-1] for i in range(len(x))]:
                    done = True
                    side = "l"
                if done:
                    break

            if done:
                p = [t[i][::-1] for i in range(len(t))][::-1]
                a[1].append([compare[0], side, p])
                break
    adjacent.append(a)

print(comp)

out = 1
top_left = -1
for a in adjacent:
    for elem in a[1]:
        if elem[1] == 'b':
            elem[1] = 't'
        elif elem[1] == 't':
            elem[1] = 'b'
        elif elem[1] == 'r':
            elem[1] = 'l'
        elif elem[1] == 'l':
            elem[1] = 'r'

adj_dict = dict()
print(adjacent)

for a in adjacent:
    if len(a[1]) == 2:
        out *= a[0]
        if a[1][0][1] == 'b' or a[1][0][1] == 'r':
            if a[1][1][1] == 'b' or a[1][1][1] == 'r':
                top_left = a[0]
    adj_dict[a[0]] = a[1]
print(top_left)
print(out)

# Assemble the map
image = [[-1 for i in range(dim)] for j in range(dim)]
image2 = [[-1 for i in range(dim)] for j in range(dim)]
x = 0
y = 0
current = top_left
while y < dim:
    print(current)
    adj = adj_dict[current]
    image[y][x] = adj[0][2]
    image2[y][x] = current 
    if x == 0:
        for a in adj:
            if a[1] == 'b':
                next_row = a[0]
    for a in adj:
        if a[1] == 'r':
            x += 1
            image[y][x] = adj_dict[a[0]][0][2]
            image2[y][x] = a[0]
            current = a[0]
            break
    if x == dim-1:
        current = next_row
        y += 1
        x = 0
print(image2)
for z in image:
    for y in z:
        for x in y:
            pass
            print(x)
        print('---------------')
    print('---------')

borderless = []
for i in image:
    new_images = []
    for j in i:
        print(j)
        new_image = []
        for y in range(1, len(j)-1):
            new_row = []
            for x in range(1, len(j)-1):
                new_row.append(j[y][x])
            new_image.append(new_row)

        new_images.append(new_image)
    borderless.append(new_images)


combined = []
for z in borderless:
    new_z = []
    for i in range(dim):
        new_row = []
        for j in range(dim):
            new_row += z[j][i]
        new_z.append(new_row)
    combined.append(new_z)

for row in combined:
    for x in row:
        pass
        #print(x)












