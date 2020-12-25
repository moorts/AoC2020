#!/usr/bin/env python3

with open('./input') as f:
    data = f.read()

decks = [list(map(int, deck.rstrip().split("\n")[1:])) for deck in data.split("\n\n")]


# True = Player 1 wins, False = Player 2 wins
def play(ds):
    played = set()
    while len(ds[0]) > 0 and len(ds[1]) > 0:
        if (tuple(ds[0]), tuple(ds[1])) in played:
            return True
        else:
            played.add((tuple(ds[0]), tuple(ds[1])))
        card1 = ds[0].pop(0)
        card2 = ds[1].pop(0)
        if len(ds[0]) >= card1 and len(ds[1]) >= card2:
            winner = play([ds[0][:card1], ds[1][:card2]])
            if winner:
                ds[0].append(card1)
                ds[0].append(card2)
            else:
                ds[1].append(card2)
                ds[1].append(card1)
        else:
            if card1 > card2:
                ds[0].append(card1)
                ds[0].append(card2)
            else:
                ds[1].append(card2)
                ds[1].append(card1)
    if len(ds[0]) > 0:
        return True
    return False

winner = play(decks)
#print(decks)
out = 0
if winner:
    for e in enumerate(decks[0]):
        out += (len(decks[0])-e[0]) * e[1]
else:
    for e in enumerate(decks[1]):
        out += (len(decks[1])-e[0]) * e[1]
print(out)
