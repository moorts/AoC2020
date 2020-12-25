with open('./input') as f:
    lines = f.readlines()

def pair_exists(x, prev):
    prev.sort()
    a = 0
    e = len(prev)-1
    while a < e:
        if prev[a] + prev[e] == x:
            return True
        elif prev[e] > x:
            e -= 1
        elif prev[a] + prev[e] > x:
            e -= 1
        elif prev[a] + prev[e] < x:
            a += 1
    return False

numbers = [int(i) for i in lines]

pre_length = 25

first_err = 0

for next_idx in range(pre_length,len(numbers)):
    num = numbers[next_idx]
    prev = numbers[next_idx-pre_length:next_idx]
    if not pair_exists(num, prev):
        first_err = num
        break

def check_set(num, l, start_idx):
    s = 0
    idx = start_idx
    while s < num:
        s += l[idx]
        idx += 1
    return (s == num, l[start_idx:idx])

def find_set(num, l):
    l.remove(num)
    start_idx = 0
    while start_idx < len(l) - 1:
        c = check_set(num, l, start_idx)
        if c[0]:
            print('Found:', c[1], min(c[1]) + max(c[1]))
            break
        start_idx += 1
find_set(first_err, numbers)
