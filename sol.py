with open('./input') as f:
    data = f.read()

groups = [line.rstrip().split("\n") for line in data.split("\n\n")]

def parse_field(field):
    name = field.split(":")[0].strip()
    desc = field.split(":")[1].strip()
    ranges = (name, [list(map(int, r.strip().split("-"))) for r in desc.split("or")])
    return ranges
fields = groups[0]
field_vals = [parse_field(field) for field in fields]
print(field_vals)

my_ticket = groups[1][1].split(",")
print(my_ticket)

nearby = [ticket.split(",") for ticket in groups[2][1:]]
print(nearby)

# Part one
valid_values = set()
for field in field_vals:
    for r in field[1]:
        for i in range(r[0], r[1]+1):
            valid_values.add(i)


error_rate = 0
delete = set()
for i in range(len(nearby)):
    for val in nearby[i]:
        if int(val) not in valid_values:
            error_rate += int(val)
            delete.add(i)
delete = list(delete)
delete.sort()
for i in delete[::-1]:
    print(i)
    nearby.pop(i)
print(nearby)
print(error_rate)

def in_range(x, r):
    if x in range(r[0][0], r[0][1]+1) or x in range(r[1][0], r[1][1]+1):
        return True
    return False

valid_ranges = field_vals
possible_classes = []
all_names = []
print(nearby)
for i in range(len(nearby[0])):
    possible = []
    names = set()
    for r in valid_ranges:
        for ticket in nearby:
            if not in_range(int(ticket[i]), r[1]):
                break
        else:
            print(ticket[i], r[1])
            possible.append(r)
            names.add(r[0])
    possible_classes.append(possible)
    all_names.append(list(names))
#possible_classes = [set([l[0] for l in p]) for p in possible_classes]
print(all_names)


idxs = dict()
def occ(c):
    count = -1
    for e in all_names:
        if c in e:
            count += 1
    return count
while len(idxs) < len(nearby[0]):
    d = [] 
    for entry in enumerate(all_names):
        for c in entry[1]:
            o = occ(c)
            if o == 0:
                idxs[c] = entry[0]
                d.append(entry[0])
    for i in d[::-1]:
        all_names[i] = []
print(idxs)
sol = 1
for k in idxs:
    if 'departure' in k:
        sol = sol * int(my_ticket[idxs[k]])
print(sol)
