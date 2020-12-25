with open('./input') as f:
    adapters = f.readlines()

adapters = [int(s.rstrip()) for s in adapters]

adapters.sort()

adapters.append(adapters[len(adapters)-1] + 3)

current_voltage = 0
differences = [0,0,0]

for a in adapters:
    if a - current_voltage <= 3:
        differences[a-current_voltage-1] += 1
        current_voltage = a

print(differences[0]*differences[2])

# Part two

# 1, 2, 3, 4
# 2, 3, 4
# 3, 4

# {
#   1: [2, 3]
#   2: [3, 4]
#   3: [4]
# }

removals = []
removals_tree = []

for i in range(1, len(adapters)-1):
    if adapters[i+1] - adapters[i-1] <= 3:
        removals.append(i)

#removals_tree.append(removals)


arrangements = 1

current_voltage = 0
differences = [0,0,0]

print(adapters)
def removable(i):
    return adapters[i+1] - adapters[i-1] <= 3

# Lets try to remove the fixed chains:
chain = []
print(len(adapters))
for i in range(len(adapters)-1):
    if adapters[i+1] - adapters[i-1] == 6:
        chain.append(i)
for i in chain[::-1]:
    del adapters[i]
del adapters[len(adapters)-1]

print(adapters)
groups = []
group = []
for i in range(len(adapters)-1):
    if adapters[i+1] - adapters[i] < 3:
        group.append(adapters[i])
    else:
        if len(group) > 0:
            group.append(adapters[i])
            groups.append(group)
            group = []
print("groups: ", groups)

def check_integrity(g, s):
    gr = g.copy()
    if s == 0:
        gr.insert(0, 0)
    for i in range(len(gr)-1):
        if gr[i+1] - gr[i] > 3:
            return False
    return True

group_combs = []

for g in groups:
    combinations = []
    if g[0] == adapters[0]:
        s = 0
    else:
        s = 1
    stack = [g]
    while len(stack) > 0:
        current = stack.pop(0)
        combinations.append(current)
        for i in range(s, len(current)-1):
            copy = current.copy()
            del copy[i]
            if check_integrity(copy, s):
                stack.append(copy)
    unique_combs = [list(x) for x in set(tuple(x) for x in combinations)]
    print(unique_combs)
    group_combs.append(len(unique_combs))

print(group_combs)
prod = 1
for c in group_combs:
    prod *= c
print(prod)

