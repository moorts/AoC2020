
while len(start) > 0:
    print(start)
    outgoing = start.pop(0)
    for square in match_dict[outgoing[0]][1]:
        print(match_dict[outgoing[0]][1])
        for mut in match_dict[square][0].mutations():
            if grid[outgoing[2]][outgoing[1]].matches(mut):
                side = grid[y][x].matches(mut)
                dx = 0
                dy = 0
                if side == 'r':
                    dx = 1
                elif side == 'b':
                    dy = 1
                #elif side == 't':
                #    dy = -1
                #elif side == 'l':
                #    dx = -1
                x = outgoing[1] + dx
                y = outgoing[2] + dy
                if grid[y][x] == '-':
                    print("grid assignment: ", square)
                    grid[y][x] = mut
                    start.append([mut.id, x, y])
