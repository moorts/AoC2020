
idxs = dict()
def occ(c):
    count = -1
    for e in possible_classes:
        if c in e:
            count += 1
    return count
while len(idxs) < len(nearby[0]):
    d = [] 
    for entry in enumerate(possible_classes):
        for c in entry[1]:
            o = occ(c)
            if o == 0:
                idxs[c] = entry[0]
                d.append(entry[0])
    for i in d[::-1]:
        possible_classes[i] = []
