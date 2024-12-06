with open("6/data.txt", "r") as file:
  data = file.read().splitlines()

data = [list(line) for line in data]

# * Part 1

WALL = "#"
GUARD = "^"

def is_inbounds(x, y):
  return x >= 0 and x < len(data) and y >= 0 and y < len(data[0])

def find_guard(data):
  for i in range(len(data)):
    for j in range(len(data[0])):
      if data[i][j] == GUARD:
        return (i, j)

START = find_guard(data)
x, y = START

# initial direction is up
dx, dy = -1, 0

steps = 0

# using a set to keep track of unique cells visited
visited = set()

while is_inbounds(x, y):
  # if the next cell is a wall, turn 90 degrees to the right
  if is_inbounds(x + dx, y + dy) and data[x + dx][y + dy] == WALL:
    if dx == -1 and dy == 0:  # up to right
      dx, dy = 0, 1
    elif dx == 1 and dy == 0:  # down to left
      dx, dy = 0, -1
    elif dx == 0 and dy == -1:  # left to up
      dx, dy = -1, 0
    elif dx == 0 and dy == 1:  # right to down
      dx, dy = 1, 0

  # move to the next cell
  x, y = x + dx, y + dy
  if not is_inbounds(x, y):
    break
  # if the cell is not walked yet, increment the steps counter
  if (x, y) not in visited:
    visited.add((x, y))
    steps += 1

print(steps)