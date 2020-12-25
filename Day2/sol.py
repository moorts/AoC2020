lines = []
with open('./input', 'r') as f:
    lines = f.readlines()

import re

lines = list(map(lambda x: x.split(), lines))

for line in lines:
    line[0] = line[0].split('-')

for line in lines:
    line[1] = line[1][0] 

count = 0
for line in lines:
    low = int(line[0][0])
    high = int(line[0][1])
    occ = line[2].count(line[1])
    if occ >= low and occ <=high:
        count += 1

print(count)
