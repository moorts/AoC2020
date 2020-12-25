lines = []
with open('./input') as f:
    lines = f.readlines()

passwords = []

password = {}

def hgt(h):
    if len(h) < 3:
        return False
    unit = h[len(h)-2:]
    num = int(h[:len(h)-2])
    if unit == 'cm':
        return num >= 150 and num <= 193
    else:
        return num >= 59 and num <= 76

def hcl(x):
    if len(x) != 7:
        return False
    if x[0] != '#':
        return False
    for c in x[1:]:
        if c not in '0123456789abcdef':
            return False

    return True

def pid(x):
    if len(x) != 9:
        return False
    for d in x:
        if d not in '0123456789':
            return False
    return True

checks = {
        'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
        'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
        'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
        'hgt': lambda x: hgt(x),
        'hcl': lambda x: hcl(x),
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: pid(x),
        'cid': lambda x: False
        }

for line in lines:
    if line == '\n':
        passwords.append(password)
        password = {}
    else:
        data = line.rstrip()
        pairs = data.split(' ')
        pairs = [pair.split(':') for pair in pairs]
        for pair in pairs:
            if checks[pair[0]](pair[1]):
                password[pair[0]] = pair[1]
            else:
                print(pair)
passwords.append(password)

#required = {'byr':True, 'iyr':True, 'eyr':True, 'hgt':True, 'hcl':True, 'ecl':True, 'pid':True}
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

count = 0
count_false = 0

for word in passwords:
    valid = True
    for key in required:
        if key not in word.keys():
            valid = False
    if valid:
        count += 1
    else:
        count_false += 1

print(len(passwords))
print(count)
