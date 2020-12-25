start = "467528193"
start = [int(c) for c in start]

idx = 0

mx = max(start)
for i in range(mx+1, 1000001):
    start.append(i)
print(len(start))

class Cup:
    def __init__(self, value):
        self.val, self.right = value, None

    def link(self, cup):
        self.right = cup

    def insert(self, cup, n=1):
        p = cup
        for _ in range(n-1):
            p = p.right
        self.right, p.right = cup, self.right


class Cups:
    def __init__(self, s, part2=False):
            self.cups = [Cup(x) for x in range(1000001 if part2 else len(s) + 1)]
            icups = list(map(int, s))
            if part2:
                icups += list(range(10, 1000001))
            for x, y in zip(icups, icups[1:]):
                self.cups[x].link(self.cups[y])
            self.cups[icups[-1]].link(self.cups[icups[0]])
            self.current = self.cups[icups[0]]
            self.size = len(self.cups) - 1
    def step(self):
        p = self.current.right
        self.current.link(p.right.right.right)
        pvals = [p.val, p.right.val, p.right.right.val, self.current.val]
        dest = self.current.val - 1 if self.current.val > 1 else self.size
        while dest in pvals:
            dest = dest - 1 if dest > 1 else self.size
        self.current = self.current.right
        self.cups[dest].insert(p, 3)

    def play(self, rounds):
        for _ in range(rounds):
            self.step()
        return self
    def get(self, key, num):
        c = self.cups[key]
        out = []
        for _ in range(num):
            c = c.right
            out.append(c.val)
        return out


import math

cups = Cups("467528193", part2=True).play(10000000)
nums = cups.get(1,2)
prod = 1
for n in nums:
    prod *= n
print(cups.get(1, 1))
print(prod)
#print("".join(map(str,out)))
