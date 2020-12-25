
k1 = 9033205
k2 = 9281649

# test values:
#k1 = 5764801
#k2 = 17807724

def handshake(ls, sbj):
    start = 1
    for i in range(ls):
        start = (start * sbj) % 20201227
    return start

i = 1
key1 = -1
key2 = -1
start = 1
while False:
    start = (start * 7) % 20201227
    if start == k1:
        key1 = i
    if start == k2:
        key2 = i
    if key1 > 0 and key2 > 0:
        break
    i += 1

print(key1, key2)

ls1 = 13467729 
ls2 = 3020524

print(handshake(ls2, k1))
print(handshake(8, 5764801))
# 
