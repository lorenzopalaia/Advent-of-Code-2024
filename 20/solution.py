from itertools import combinations

# * Part 1

# ! IDEA: Flood fill the grid to get all distances from the start position

with open("20/data.txt", "r") as file:
    data = file.read().strip()

# Create a dictionary with positions as keys and characters as values
grid = {i + j * 1j: c for i, row in enumerate(data.split('\n'))
        for j, c in enumerate(row) if c != '#'}

# Find the start position
start_pos, = (pos for pos in grid if grid[pos] == 'S')

# Initialize the distance dictionary and the list of positions to process
dists = {start_pos: 0}
pos_to_process = [start_pos]

# Perform a BFS to calculate distances from the start position
for cur_pos in pos_to_process:
    for new_pos in [cur_pos - 1, cur_pos + 1, cur_pos - 1j, cur_pos + 1j]:
        if new_pos in grid and new_pos not in dists:
            dists[new_pos] = dists[cur_pos] + 1
            pos_to_process.append(new_pos)

res = 0

# Check all combinations of positions and their distances
for (pos1, dist1), (pos2, dist2) in combinations(dists.items(), 2):
    manhattan_dist = abs((pos1 - pos2).real) + abs((pos1 - pos2).imag)
    if manhattan_dist == 2 and dist2 - dist1 - manhattan_dist >= 100:
        res += 1

print(res)
