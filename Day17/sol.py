
def adj(l, sub=[]):
    if not l:
        yield sub
    else:
        yield from [idx for j in range(l[0]-1, l[0]+2) for idx in adj(l[1:], sub + [j])]

def in_m(m, p):
    if p[0] < 0 or p[0] >= len(m):
        return False
    if p[1] < 0 or p[1] >= len(m[0]):
        return False
    if p[2] < 0 or p[2] >= len(m[0][0]):
        return False
    if p[3] < 0 or p[3] >= len(m[0][0][0]):
        return False
    return True

with open('./input') as f:
    initial = f.readlines()

initial = [[char for char in line.rstrip()] for line in initial]

matrix = [[initial]]
print(matrix)

width = len(matrix[0][0])
length = len(matrix[0][0])

z_i = 1
y_i = 1
x_i = 1
w_i = 1
cycles = 0

width += 2
length += 2
while cycles < 6:
    new_matrix = []
    for w in range(len(matrix)+2):
        new_w_plane = []
        for i in range(len(matrix[0])+2):
            new_layer = [['.' for i in range(width)] for i in range(length)]
            new_w_plane.append(new_layer)
        new_matrix.append(new_w_plane)

    for w in range(len(new_matrix)):
        for z in range(len(new_matrix[w])):
            for y in range(len(new_matrix[w][z])):
                for x in range(len(new_matrix[w][z][y])):
                    point = (w-w_i, z - z_i, y-y_i, x-x_i)
                    adjacents = adj(point)
                    active_neighbours = 0
                    for a in adjacents:
                        if a[0] == point[0] and a[1] == point[1] and a[2] == point[2] and a[3] == point[3]:
                            continue
                        if in_m(matrix, a):
                            if matrix[a[0]][a[1]][a[2]][a[3]] == '#':
                                active_neighbours += 1
                    if in_m(matrix, point):
                        status = matrix[point[0]][point[1]][point[2]][point[3]]
                    else:
                        status = '.'
                    if status == '#':
                        if active_neighbours < 2 or active_neighbours > 3:
                            new_matrix[w][z][y][x] = '.'
                        else:
                            new_matrix[w][z][y][x] = '#'
                    else:
                        if active_neighbours == 3:
                            new_matrix[w][z][y][x] = '#'

    cycles += 1
    width += 2
    length += 2
    count = 0
    matrix = [[line.copy() for line in plane] for plane in new_matrix]
    for w_plane in new_matrix:
        for plane in w_plane:
            for line in plane:
                for c in line:
                    if c == '#':
                        count += 1
                print(line)
            print('-----------')
    print('Count: ', count)

