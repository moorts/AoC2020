with open('./input') as f:
    instructions = f.readlines()

instructions = [(i[:1], i.rstrip()[1:]) for i in instructions]

# Directions: North = 0, East = 1, South = 2, West = 3
direction_idx = 1
directions = ['N', 'E', 'S', 'W']

east_west = 0
north_south = 0

for i in instructions:
    action = i[0]
    arg = int(i[1])
    if action == 'L':
        direction_idx = (direction_idx - (arg // 90)) % 4
    elif action == 'R':
        direction_idx = (direction_idx + (arg // 90)) % 4
    if action == 'F':
        action = directions[direction_idx]
    if action == 'N':
        north_south += arg
    elif action == 'S':
        north_south -= arg
    elif action == 'E':
        east_west += arg
    elif action == 'W':
        east_west -= arg

print(abs(east_west) + abs(north_south))

