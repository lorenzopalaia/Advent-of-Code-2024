with open("18/data.txt", "r") as file:
    data = [tuple(map(int, line.strip().split(","))) for line in file]

START = (0, 0)
EXIT = (70, 70)
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_shortest_path(data):
    visiteds = set()
    positions_to_visit = [(START, 0)]

    while positions_to_visit:
        current, current_distance = positions_to_visit.pop(0)

        if current in visiteds:
            continue

        if current == EXIT:
            return current_distance

        for dx, dy in DIRS:
            next = current[0] + dx, current[1] + dy
            if 0 <= next[0] <= 70 and 0 <= next[1] <= 70 and next not in visiteds and next not in data:
                positions_to_visit.append((next, current_distance + 1))

        visiteds.add(current)

    return None


# * Part 1

# ! IDEA: Find the shortest path from START to EXIT using the first 1024 obstacles in the data.

res = find_shortest_path(data[:1024])
print(res)

# * Part 2

# ! IDEA: Use binary search to find the minimum number of obstacles that still allows a path from START to EXIT.

lower_bound = 1024
upper_bound = len(data)

while upper_bound - lower_bound > 1:
    mid_point = (lower_bound + upper_bound) // 2

    if find_shortest_path(data[:mid_point]):
        lower_bound = mid_point
    else:
        upper_bound = mid_point

res = data[upper_bound - 1]
print(res)
