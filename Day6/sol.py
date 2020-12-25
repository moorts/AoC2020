
with open('./input') as f:
    inp = f.readlines()

groups = []
group = ""

for line in inp:
    if line == '\n':
        groups.append(group)
        group = ""
    else:
        group += line.rstrip()

groups.append(group)

charsets = []

for g in groups:
    s = set()
    for c in g:
        s.add(c)
    charsets.append(s)

print(sum(map(len, charsets)))
