a = [
        "ababbb",
        "bababa",
        "abbbab",
        "aaabbb",
        "aaaabbb"
    ]

import re
from parse import *

r = re.compile("a(((aa|bb)(ab|ba))|((ab|ba)(aa|bb)))b$")

with open('./input') as f:
    data = f.read()

data = data.split("\n\n")

rules = data[0].split("\n")
messages = data[1].split("\n")

r = dict()
for rule in rules:
    rule = rule.split(': ')
    if rule[1][0] == '"':
        r[rule[0]] = rule[1][1]
    else:
        subs = [s.split(' ') for s in rule[1].split(' | ')]
        r[rule[0]] = subs

def construct_regex(r, rule):
    if not rule in r:
        raise ValueError('Rule doesnt exist')
    if isinstance(r[rule], str):
        return r[rule]
    ors = []
    for entry in r[rule]:
        o = ''
        for x in entry:
            o += construct_regex(r, x)
        ors.append(o)
    regex = "(" + ors[0] + ""
    for o in ors[1:]:
        regex += "|" + o
    return regex + ")"

def create_regex(r, rule):
    return construct_regex(r, rule) + "$"

#r = re.compile(create_regex(r, "0"))
print(r)
print(construct_regex(r, '42'))

count = 0

def check(message):
    st42 = construct_regex(r, '42')
    st31 = construct_regex(r, '31')


    r42 = f"({st42})"
    r31 = f"({st31})"
    count = 0
    length = 0
    while length < len(message):
        m = re.compile(r42).match(message)
        if not m:
            break
        elif m.span()[1] == length:
            break
        length = m.span()[1]
        count += 1
        if count > 1:
            count31 = 0
            while count31 < count-1:
                print(count31, count-1)
                if re.compile(f"{r31}$").match(message[length:]):
                    return True
                elif re.compile(r31).match(message[length:]):
                    r31 = f"{r31}({st31})"
                    count31 += 1
                else:
                    break

        r42 = f"{r42}({st42})"
    print(count)
    return False

for m in messages:
    if check(m):
        count+= 1
print(count)

