with open('./input') as f:
    data = f.readlines()

equations = [line.rstrip().split(" ") for line in data]

test = "1 + 2 * 3 + 4 * 5 + 6"
test = test.split(" ")

def format_equation(e):
    out = []
    for operand in e:
        start_parentheses = 0
        for i in range(len(operand)):
            if operand[i] != '(':
                break
            else:
                start_parentheses += 1
        end_parentheses = 0
        for i in range(len(operand))[::-1]:
            if operand[i] != ')':
                break
            else:
                end_parentheses += 1
        new_ps = [p for p in operand[:start_parentheses]]
        new_pe = [p for p in operand[len(operand)-end_parentheses:]]
        new_operand = new_ps + [operand[start_parentheses:len(operand)-end_parentheses]] + new_pe
        out += new_operand
    return out


def eval(t):
    operations = []
    i = 0
    while i < len(t):
        if t[i] == '(':
            o = 1
            end = i+1
            while t[end] != ')' or o > 1:
                if t[end] == '(':
                    o += 1
                elif t[end] == ')':
                    o -= 1
                end += 1
            t = t[:i] + [eval(t[i+1:end])] + t[end+1:]
        i += 1
    return eval_flat_a_first(t)


def eval_flat(t):
    res = 0
    while len(t) > 1:
        first = t[0]
        second = t[2]
        if t[1] == '+':
            s = int(first) + int(second)
        else:
            s = int(first) * int(second)
        t = [str(s)] + t[3:]
    return t[0]

def eval_flat_a_first(t):
    res = 0
    i = 0
    while i < len(t)-1:
        if t[i+1] != '+':
            i += 2
        else:
            first = t[i]
            second = t[i+2]
            s = int(first) + int(second)
            t = t[:i] + [str(s)] + t[i+3:]
    return eval_flat(t)





format_equation(equations[0])
equations = [format_equation(e) for e in equations]
s = 0
for e in equations:
    s += int(eval(e))
print(s)
