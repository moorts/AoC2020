with open('./input') as f:
    data = f.readlines()

data = [line.rstrip().split(" ") for line in data]
data = [(l[0], l[2]) for l in data]
print(data)

def dec_to_bin(dec):
    b = bin(dec)[2:]
    return (36 - len(b)) * '0' + b

def bin_to_dec(dec):
    return int(dec, 2)

def apply_mask(val, mask):
    vl = [char for char in val] 
    for i in range(len(vl)):
        if mask[i] != 'X':
            vl[i] = mask[i]
    return "".join(vl)


mask = 'X' * 36
mem = {}

for command in data:
    if command[0] == 'mask':
        mask = command[1]
    else:
        address = command[0].split('[')[1].rstrip(']')
        mem[address] = bin_to_dec(apply_mask(dec_to_bin(int(command[1])), mask))

s = 0
for k in mem:
    s += mem[k]

print(s)
