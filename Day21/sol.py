with open('./input') as f:
    data = f.readlines()

data = [line.rstrip() for line in data]

ingredients = [line[:-1].split('(contains ') for line in data]
ingredients = [[line[0].split(' ')[:-1], line[1].replace(",", "").split(' ')] for line in ingredients]
print(ingredients)

p = dict()

u_i = set()
for i in ingredients:
    for food in i[0]:
        u_i.add(food)

for i in ingredients:
    for allerg in i[1]:
        if allerg not in p:
            p[allerg] = i[0]
        else:
            foods = []
            for food in p[allerg]:
                if food in i[0]:
                    foods.append(food)
            p[allerg] = foods

print(p)

guaranteed = set()
count = 0
while 1:
    removed = 0
    for k, v in p.items():
        if len(v) < 2:
            guaranteed.add(v[0])
        else:
            for food in v:
                if food in guaranteed:
                    v.remove(food)
                    removed += 1
    if removed == 0:
        print(count)
        break
    count += 1
print(guaranteed)
out = 0
for i in ingredients:
    for food in i[0]:
        if food not in guaranteed:
            out += 1

danger = ""
allergens = p.keys()
allergens = list(allergens)
allergens.sort()
for a in allergens:
    danger += p[a][0] + ','

print(danger[:-1])


     
