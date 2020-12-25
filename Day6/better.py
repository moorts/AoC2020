with open('./input') as f:
    data = f.read()

groups = [group.rstrip().split("\n") for group in data.split("\n\n")]

any_yes = 0
all_yes = 0

for group in groups:
    p1 = set(group[0])
    p2 = set(group[0])
    for line in group[1:]:
        p1 |= set(line)
        p2 &= set(line)
    any_yes += len(p1)
    all_yes += len(p2)

    
print(any_yes, all_yes)
