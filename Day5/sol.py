def calc_seat(port, s, e, zero_char):

    row = port[s:e]

    row = [0 if c == zero_char else 1 for c in row]

    n = 0

    for i in range(e-s):
        p = 2**(e-s-1-i)
        n += row[i] * p

    return n

def calc_row(port):
    return calc_seat(port, 0, 7, 'F')

def calc_col(port):
    return calc_seat(port, 7, 10, 'L')

lines = []

with open('./input') as f:
    lines = f.readlines()

ids = []
for line in lines:
    row = calc_row(line)
    col = calc_col(line)
    ID = row * 8 + col
    ids.append(ID)

ids.sort()
for i in range(len(ids)-1):
    if ids[i]+1 != ids[i+1]:
        print(ids[i]+1)
#print(max(ids))
