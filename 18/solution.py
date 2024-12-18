with open("18/data.txt", "r") as file:
    data = [tuple(map(int, l.strip().split(","))) for l in file]


START = (0, 0)
END = (70, 70)

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def maze(data):

    visited = set()
    to_visit = [(START, 0)]

    while to_visit:
        cp, cd = to_visit.pop(0)

        if cp in visited:
            continue

        if cp == END:
            return cd

        for dx, dy in DIRS:
            np = cp[0] + dx, cp[1] + dy
            if 0 <= np[0] <= 70 and 0 <= np[1] <= 70 and np not in visited and np not in data:
                to_visit.append((np, cd + 1))

        visited.add(cp)

    return None


res = maze(data[:1024])
print(res)
