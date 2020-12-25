
with open('./input') as f:
    data = f.readlines()

data = [line.rstrip().split(" ") for line in data]
data = [(l[0], l[2]) for l in data]

def dec_to_bin(dec, pad=36):
    b = bin(dec)[2:]
    return (pad - len(b)) * '0' + b

def bin_to_dec(dec):
    return int(dec, 2)

def apply_mask(val, mask):
    vl = [char for char in val] 
    for i in range(len(vl)):
        if mask[i] != '0':
            vl[i] = mask[i]

    return "".join(vl)

def get_addresses(address):
    x_c = address.count('X')
    addresses = []
    for i in range(2**x_c):
        floating = dec_to_bin(i, pad=x_c)
        new_a = [char for char in address]
        idx = 0
        for j in range(len(new_a)):
            if new_a[j] == 'X':
                new_a[j] = floating[idx]
                idx += 1
        addresses.append(bin_to_dec("".join(new_a)))
    return addresses




mask = 'X' * 36
mem = {}

for command in data:
    if command[0] == 'mask':
        mask = command[1]
    else:
        address = command[0].split('[')[1].rstrip(']')
        a = apply_mask(dec_to_bin(int(address)), mask)
        adds = get_addresses(a)
        for add in adds:
            mem[add] = int(command[1])

s = 0
for k in mem:
    s += mem[k]

print(s)
