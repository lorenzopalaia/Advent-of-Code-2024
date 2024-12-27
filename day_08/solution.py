with open("8/data.txt", "r") as file:
  grid = [list(line.strip()) for line in file]

antenna_map = []
frequencies = set()

# * Constants
EMPTY = "."
ANTINODE = "#"

# * Helper Functions
def is_inbounds(x, y, grid):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

# Calculates the slope (rise and run) between two antenna positions
def find_slope(ant_a, ant_b):
  x1, y1 = ant_a
  x2, y2 = ant_b
  return abs(y2 - y1), abs(x2 - x1)

# Computes the first antinodes between two antennas
def compute_antinode(ant_a, ant_b):
  rise, run = find_slope(ant_a, ant_b)
  x1, y1 = ant_a
  x2, y2 = ant_b

  # Adjust positions to extend antinodes
  if x1 > x2:
    x1 += run
    x2 -= run
  elif x1 < x2:
    x1 -= run
    x2 += run

  if y1 < y2:
    y1 -= rise
    y2 += rise

  return (x1, y1), (x2, y2)

# Computes all antinodes within bounds between two antennas
def compute_antinode_with_bounds(ant_a, ant_b):
  rise, run = find_slope(ant_a, ant_b)
  x1, y1 = ant_a
  x2, y2 = ant_b

  antinodes = [(x1, y1), (x2, y2)]
  in_bounds1, in_bounds2 = True, True

  # Generate antinodes until one or both positions go out of bounds
  while in_bounds1 or in_bounds2:
    if x1 > x2:
      x1 += run
      x2 -= run
    elif x1 < x2:
      x1 -= run
      x2 += run

    if y1 < y2:
      y1 -= rise
      y2 += rise

    if not is_inbounds(x1, y1, grid):
      in_bounds1 = False
    else:
      antinodes.append((x1, y1))

    if not is_inbounds(x2, y2, grid):
      in_bounds2 = False
    else:
      antinodes.append((x2, y2))

  return antinodes

# Parse the input to map antennas and identify unique frequencies
for y, row in enumerate(grid):
  for x, char in enumerate(row):
    if char != EMPTY:
      frequencies.add(char)
      antenna_map.append((char, (x, y)))

# * Part 1
antinode_set_part1 = set()

for freq in frequencies:
  antennas = [ant[1] for ant in antenna_map if ant[0] == freq]
  for i, ant_a in enumerate(antennas):
    for j in range(i + 1, len(antennas)):
      antinode_a, antinode_b = compute_antinode(ant_a, antennas[j])
      antinode_set_part1.add(antinode_a)
      antinode_set_part1.add(antinode_b)

part1 = 0
for x, y in antinode_set_part1:
  if is_inbounds(x, y, grid):
    part1 += 1
    grid[y][x] = ANTINODE

print(part1)

# * Part 2
antinode_set_part2 = set()

for freq in frequencies:
  antennas = [ant[1] for ant in antenna_map if ant[0] == freq]
  for i, ant_a in enumerate(antennas):
    for j in range(i + 1, len(antennas)):
      antinodes = compute_antinode_with_bounds(ant_a, antennas[j])
      antinode_set_part2.update(antinodes)

part2 = 0
for x, y in antinode_set_part2:
  if is_inbounds(x, y, grid):
    part2 += 1
    grid[y][x] = ANTINODE

print(part2)