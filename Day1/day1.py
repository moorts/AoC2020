lines = []

with open('./input', 'r') as f:
    lines = f.readlines()

lines = list(map(int, lines))

from itertools import combinations
from numpy import prod

print(prod(list(filter(lambda x: sum(x) == 2020, combinations(lines, 3)))[0]))
