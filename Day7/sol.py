with open('./input') as f:
    lines = f.readlines()

lines = [line.split(',') for line in lines]

lines = [[i.split(' ') for i in line] for line in lines]




bags = dict()

for line in lines:
    color = ' '.join(line[0][:2])
    colors = []
    for quant in line[1:]:
        c = ' '.join(quant[2:4])
        colors.append((int(quant[1]), c))
    if line[0][4] != 'no':
        last_c = ' '.join(line[0][5:7])
        colors.append((int(line[0][4]), last_c))
    else:
        colors.append((0, ''))
    if color in bags:
        bags[color].extend(colors)
    else:
        bags[color] = colors


shiny_gold = 0

# Part one

for color in bags:
    bags_to_search = bags[color].copy()
    shiny_gold_reachable = False
    while len(bags_to_search) > 0:
        top = bags_to_search.pop(0)
        if top[1] == 'shiny gold':
            shiny_gold_reachable = True
            break
        if top[0] != 0:
            bags_to_search.extend(bags[top[1]])
    if shiny_gold_reachable:
        shiny_gold += 1


# Part two
def quantities(bag):
    if bag[0] == 0:
        return 0
    else:
        out = bag[0]
        inner_bags = 0
        print(bag)
        for b in bags[bag[1]]:
            inner_bags += quantities(b)
        return out * inner_bags + bag[0]

other_bags = 0
bag_quantities = bags['shiny gold']
print(sum(map(quantities, bag_quantities)))



print(shiny_gold)

