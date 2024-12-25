with open("25/data.txt", "r") as file:
    data = file.read().split('\n\n')

items = []
for item in data:
    item_set = {i for i, c in enumerate(item) if c == '#'}
    items.append(item_set)

res = 0
for keys in items:
    for locks in items:
        if not keys & locks:
            res += 1
res //= 2
print(res)
