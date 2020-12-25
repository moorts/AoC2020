with open('./input') as f:
    instructions = f.readlines()

instructions = [(i[:1], i.rstrip()[1:]) for i in instructions]

# Directions: North = 0, East = 1, South = 2, West = 3

east_west = 0
north_south = 0

w_east_west = 10
w_north_south = 1

for i in instructions:
    action = i[0]
    arg = int(i[1])
    if action == 'F':
        east_west += (w_east_west * arg)
        north_south += (w_north_south * arg)
    if action == 'L':
        turns = arg // 90
        for t in range(turns):
            if w_north_south >= 0:
                if w_east_west >= 0:
                    temp = w_north_south
                    w_north_south = w_east_west
                    w_east_west = -temp
                elif w_east_west < 0:
                    temp = w_east_west
                    w_east_west = -w_north_south
                    w_north_south = temp
            elif w_north_south < 0:
                if w_east_west >= 0:
                    temp = w_east_west
                    w_east_west = -w_north_south
                    w_north_south = temp
                elif w_east_west < 0:
                    temp = w_north_south
                    w_north_south = w_east_west
                    w_east_west = -temp
    elif action == 'R':
        turns = arg // 90
        for t in range(turns):
            if w_north_south >= 0:
                if w_east_west >= 0:
                    temp = w_east_west
                    w_east_west = w_north_south
                    w_north_south = -temp
                elif w_east_west < 0:
                    temp = w_north_south
                    w_north_south = -w_east_west
                    w_east_west = temp
            elif w_north_south < 0:
                if w_east_west >= 0:
                    temp = w_north_south
                    w_north_south = -w_east_west
                    w_east_west = temp
                elif w_east_west < 0:
                    temp = w_north_south
                    w_north_south = -w_east_west
                    w_east_west = temp
    if action == 'N':
        w_north_south += arg
    elif action == 'S':
        w_north_south -= arg
    elif action == 'E':
        w_east_west += arg
    elif action == 'W':
        w_east_west -= arg

print(abs(east_west) + abs(north_south))

