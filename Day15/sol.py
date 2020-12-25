with open('./input') as f:
    data = f.read()

numbers = data.rstrip().split(',')
print(numbers)

last_spoken = dict()

turn = 1

last_number = ''

for number in numbers:
    if last_number != '':
        last_spoken[last_number] = turn-1
    last_number = number
    turn += 1

while len(numbers) < 30000000:
    if last_number not in last_spoken:
        next_number = '0'
    else:
        next_number = str(turn-1 - int(last_spoken[last_number]))

    last_spoken[last_number] = turn-1
    last_number = next_number
    numbers.append(next_number)
    turn += 1

print(last_spoken)
print(numbers[30000000-1])
