
with open('./input') as f:
    data = f.readlines()

stamps = [x for x in data[1].rstrip().split(',')]

# 13 * x = 7*y + 1
# y = (13*x -1) / 7

y = 1
iid = int(stamps[0])
idx = 0
for i in range(1, len(stamps)):
    if stamps[i] != 'x':
        if idx == 0 or int(stamps[i]) < int(stamps[idx]):
            idx = i
searching = True
found_first = False
increment = 1
intersections = {}
for i in range(1,len(stamps)):
    if stamps[i] != 'x':
        fac = 1
        inc = 1
        while True:
            if (iid*fac + i) % int(stamps[i]) == 0:
                intersections[int(stamps[i])] = fac
                break
            fac += 1

next_idx = 1
stamps = [(stamps.index(x), int(x)) for x in stamps if x != 'x']
print(stamps)
found = [0]
seen = -1
while searching:
    for f in found:
        if (iid*y + stamps[f][0]) % stamps[f][1] != 0:
            break
    else:
        print(found, y, increment)
        if (iid*y + stamps[next_idx][0]) % stamps[next_idx][1] == 0:
            if len(found) == len(stamps) -1:
                for i in range(len(stamps)):
                    if (iid*y + stamps[i][0]) % int(stamps[i][1]) != 0:
                        break
                else:
                    print(iid*y, "found it")
                    break
            if seen == -1:
                print('seen:', y)
                seen = y
            else:
                found.append(next_idx)
                increment = y - seen
                next_idx += 1
                seen = -1


    y += increment



# 7*y + 1 = t1 * x1 -> t1 * x1 -1 = t2 * x2 -2 -> t1 * x1 + 1= t2 * x2 -> x2 = (t1 * x1 + 1) / t2
# 7*y + 2 = t2 * x2
# ...
# 7*y + n = tn + xn
