with open('./input') as f:
    data = f.readlines()

e = int(data[0].rstrip())
stamps = [x for x in data[1].rstrip().split(',')]

min_id = -1
d = -1
for s in stamps:
    if s != 'x':
        bid = int(s)
        factor = e // bid
        earliest = bid * factor + bid
        diff = earliest - e
        if min_id == -1:
            min_id = bid
            d = diff
        if diff < d:
            min_id = bid
            d = diff

print(min_id *d)


