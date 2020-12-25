lines = []
with open('./input', 'r') as f:
    lines = f.readlines()

import re

lines = list(map(lambda x: x.split(), lines))

for line in lines:
    line[0] = line[0].split('-')
    line[1] = line[1][0] 

count = 0
for line in lines:
    low = int(line[0][0]) - 1
    high = int(line[0][1]) - 1
    first = line[2][low] == line[1]
    second = line[2][high] == line[1]
    if first ^ second:
        count += 1


print(count)
