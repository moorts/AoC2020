with open('./input') as f:
    lines = f.readlines()

lines = [line.split(' ') for line in lines]
for line in lines:
    line[1] = int(line[1])

#print(lines)

ex_count = [0 for line in lines]

ip = 0

acc = 0

for line in lines:
    # Flip instruction or skip iteration
    if line[0] == 'nop':
        line[0] = 'jmp'
    elif line[0] == 'jmp':
        line[0] = 'nop'
    else:
        continue

    while ip < len(lines):
        instruction = lines[ip]
        #print(instruction, i)
        if ex_count[ip] > 0:
            break
        ex_count[ip] = ex_count[ip] + 1
        if instruction[0] == 'nop':
            ip += 1
        elif instruction[0] == 'acc':
            acc += instruction[1]
            ip += 1
        else:
            ip += instruction[1]
    if ip == len(lines):
        print('success', acc)
        break

    # Flip instruction back
    if line[0] == 'nop':
        line[0] = 'jmp'
    elif line[0] == 'jmp':
        line[0] = 'nop'
    ex_count = [0 for line in lines]
    ip = 0
    acc = 0

def execute(instructions):
    pc = 0
    accumulator = 0
    instruction_count = [0 for i in instructions]
    while pc < len(lines):
        instruction = instructions[pc]
        if instruction_count[pc] > 0:
            print("Endless loop")
            break
        ex_count[pc] = ex_count[pc] + 1
        if instruction[0] == 'nop':
            pc += 1
        elif instruction[0] == 'acc':
            accumulator += instruction[1]
            pc += 1
        else:
            pc += instruction[1]
    return accumulator
