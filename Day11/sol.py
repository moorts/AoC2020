with open('./input') as f:
    data = f.readlines()

seats = [[c for c in l.strip()] for l in data]

width = len(seats[0])
height = len(seats)

# Create AdjacentSeat Dictionary

adj_coords = dict()
for y in range(height):
    for x in range(width):
        if seats[y][x] == '.':
            continue
        adj_coords[(y,x)] = []
        x_right = 1
        while x_right + x < width:
            if seats[y][x_right + x] != '.':
                break
            x_right += 1
        if x_right + x == width:
            adj_coords[(y, x)].append((-1, -1))
        else:
            adj_coords[(y, x)].append((y, x + x_right))
        x_left = 1
        while x - x_left >= 0:
            if seats[y][x - x_left] != '.':
                break
            x_left += 1
        if x - x_left == -1:
            adj_coords[(y, x)].append((-1, -1))
        else:
            adj_coords[(y, x)].append((y, x - x_left))
        y_top = 1
        while y - y_top >= 0:
            if seats[y - y_top][x] != '.':
                break
            y_top += 1
        if y - y_top == -1:
            adj_coords[(y, x)].append((-1, -1))
        else:
            adj_coords[(y, x)].append((y - y_top, x))
        y_bot = 1
        while y + y_bot < height:
            if seats[y + y_bot][x] != '.':
                break
            y_bot += 1
        if y + y_bot == height:
            adj_coords[(y, x)].append((-1, -1))
        else:
            adj_coords[(y, x)].append((y + y_bot, x))
        diag = 1
        while y - diag >= 0 and x + diag < width:
            if seats[y - diag][x + diag] != '.':
                break
            diag += 1
        if y - diag == -1 or x + diag == width:
            adj_coords[(y, x)].append((-1, -1))
        else:
            adj_coords[(y, x)].append((y - diag, x + diag))
        diag = 1
        while y - diag >= 0 and x - diag >= 0:
            if seats[y - diag][x - diag] != '.':
                break
            diag += 1
        if y - diag == -1 or x - diag == -1:
            adj_coords[(y, x)].append((-1, -1))
        else:
            adj_coords[(y, x)].append((y - diag, x - diag))
        diag = 1
        while y + diag < height and x + diag < width:
            if seats[y + diag][x + diag] != '.':
                break
            diag += 1
        if y + diag == height or x + diag == width:
            adj_coords[(y, x)].append((-1, -1))
        else:
            adj_coords[(y, x)].append((y + diag, x + diag))
        diag = 1
        while y + diag < height and x - diag >= 0:
            if seats[y + diag][x - diag] != '.':
                break
            diag += 1
        if y + diag == height or x - diag == -1:
            adj_coords[(y, x)].append((-1, -1))
        else:
            adj_coords[(y, x)].append((y + diag, x - diag))
print(adj_coords[(6,2)])

def adjacent_seats(x, y):
    adjacent = 0
    for (j, i) in adj_coords[(y, x)]:
        if i < 0 or i >= width:
            continue
        if j < 0 or j >= height:
            continue
        if y == 0 and x == 3:
            print(j, i, seats[j][i])
        if seats[j][i] == '#':
            if y == 0 and x == 3:
                print('# found')
            adjacent += 1
    return adjacent

new_seats = [['-' for _ in range(width)] for _ in range(height)]
iterations = 0

while True:
    unchanged = 0
    for y in range(height):
        for x in range(width):
            seat = seats[y][x]
            if seat == '.':
                new_seats[y][x] = '.'
                unchanged += 1
                continue
            occ = adjacent_seats(x, y)
            if seat == 'L' and occ == 0:
                new_seats[y][x] = '#'
            elif seat == '#' and occ >= 5:
                new_seats[y][x] = 'L'
            else:
                new_seats[y][x] = seat
                unchanged += 1
    iterations += 1
    if unchanged == height * width:
        print('Success:', iterations)
        break

    seats = [l.copy() for l in new_seats.copy()]

occupied = 0
for y in range(height):
    for x in range(width):
        if seats[y][x] == '#':
            occupied += 1

print(occupied)

