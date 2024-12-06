with open("6/data.txt", "r") as file:
  data = file.read().splitlines()

data = [list(line) for line in data]

# * Constants
WALL = "#"
GUARD = "^"

# * Helper Functions
def is_inbounds(x, y, data):
  return 0 <= x < len(data) and 0 <= y < len(data[0])

def find_guard(data):
  for i in range(len(data)):
    for j in range(len(data[0])):
      if data[i][j] == GUARD:
        return (i, j)
  return None

# * Part 1
START = find_guard(data)
visited = set()
x, y = START
dx, dy = -1, 0  # initial direction: up

while is_inbounds(x, y, data):
  # Determine the next position
  next_x, next_y = x + dx, y + dy

  # If there's a wall, turn 90 degrees to the right
  if is_inbounds(next_x, next_y, data) and data[next_x][next_y] == WALL:
    dx, dy = dy, -dx
  else:
    # Move forward and add the position to visited cells
    x, y = next_x, next_y
    visited.add((x, y))

print(len(visited) - 1)  # Subtract 1 to exclude the starting position

# * Part 2
loops = 0

for obs_x, obs_y in visited - {START}:
  # Place an obstacle
  data[obs_x][obs_y] = WALL

  # Restart simulation
  seen = set()
  x, y = START
  dx, dy = -1, 0  # initial direction: up
  is_loop = False

  while is_inbounds(x, y, data):
    next_x, next_y = x + dx, y + dy

    # If there's a wall, turn 90 degrees to the right
    if is_inbounds(next_x, next_y, data) and data[next_x][next_y] == WALL:
      dx, dy = dy, -dx
    else:
      # Move forward
      x, y = next_x, next_y

      # Check if the current state has been seen before
      if (x, y, dx, dy) in seen:
        is_loop = True
        break

      seen.add((x, y, dx, dy))

    # Remove the obstacle
  data[obs_x][obs_y] = "."

  if is_loop:
    loops += 1

print(loops)