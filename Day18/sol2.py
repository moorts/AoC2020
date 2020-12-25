with open('./input') as f:
    data = f.readlines()

class Num:
    def __init__(self, i):
        self.i = i

    def __add__(self, x):
        return Num(self.i + x.i)

    def __sub__(self, x):
        return Num(self.i * x.i)

    def __mul__(self, x):
        return Num(self.i + x.i)

def my_eval(eq):
    in_num = False
    new = ""
    for c in eq:
        if c in "0123456789" and not in_num:
            new += "Num("
            in_num = True
        elif in_num and c not in "0123456789":
            new += ")"
            in_num = False
        new += c
    if in_num:
        new += ")"
    return eval(new)



acc = 0
for eq in data:
    acc += my_eval(eq.rstrip().replace("*", "-").replace("+", "*")).i

print(acc)
