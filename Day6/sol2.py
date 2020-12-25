
with open('./input') as f:
    inp = f.readlines()

groups = []
group = []

for line in inp:
    if line == '\n':
        groups.append(group)
        group = []
    else:
        group.append(line.rstrip())

groups.append(group)

charsets = []

for g in groups:
    d = dict()
    for person in g:
        for answer in person:
            if answer in d:
                d[answer] += 1
            else:
                d[answer] = 1
    pcount = len(g)
    r = []
    for k in d:
        if d[k] != pcount:
            r.append(k)
    for k in r:
        d.pop(k)
    charsets.append(d)

#print(charsets)
print(sum(map(len, charsets)))
