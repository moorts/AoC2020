lines = []

with open('./input') as f:
    lines = f.readlines()

lines = [[c for c in line.rstrip()] for line in lines]

xvels = [1,3,5,7,1]
yvels = [1,1,1,1,2]
vels = list(zip(xvels, yvels))


trees = []
idx = 0
for vel in vels:
    x = 0
    y = 0
    xvel = vel[0]
    yvel = vel[1]
    print(xvel, yvel)
    trees.append(0)
    while y < len(lines):
        if lines[y][x] == '#':
            trees[idx] += 1
        x = (x + xvel) % len(lines[0])
        y += yvel
    idx += 1


out = 1
for t in trees:
    out = out * t

print(out)
