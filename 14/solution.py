with open("14/data.txt", "r") as file:
    data = file.read().splitlines()

positions = []
velocities = []

for line in data:
    p, v = line.split(' ')
    p = p.split('=')[1].split(',')
    v = v.split('=')[1].split(',')
    positions.append((int(p[0]), int(p[1])))
    velocities.append((int(v[0]), int(v[1])))

max_x = max(positions, key=lambda pos: pos[0])[0] + 1
max_y = max(positions, key=lambda pos: pos[1])[1] + 1


def simulate_robot(position, velocity, steps):
    px, py = position
    vx, vy = velocity
    return ((px + vx * steps) % max_x, (py + vy * steps) % max_y)


def count_by_quadrant(positions):
    middle_x = max_x // 2
    middle_y = max_y // 2

    quadrant_counts = [0, 0, 0, 0]
    for position in positions:
        x, y = position
        if x != middle_x and y != middle_y:
            quadrant_id = 2 * (x < middle_x) + (y < middle_y)
            quadrant_counts[quadrant_id] += 1

    return quadrant_counts


def find_easter_egg(positions, velocities):
    lines = [set((x, y) for x in range(max_x)) for y in range(max_y)]

    for step in range(max_x * max_y):
        robot_positions = set(simulate_robot(position, velocity, step)
                              for position, velocity in zip(positions, velocities))
        max_line, y = max((len(robot_positions & line), y)
                          for y, line in enumerate(lines))

        if max_line >= 30:
            contiguous = 0
            for x in range(max_x):
                if (x, y) in robot_positions:
                    contiguous += 1
                else:
                    contiguous = 0
                if contiguous == 30:
                    return step


# * Part 1

# ! IDEA: simulate robot movement with the law of physics
# ! robots move by uniform linear motion so we can use the formula
# ! position = initial_position + velocity * time
# ! we can handle the wrapping around the grid by using modulo operator

final_positions = [simulate_robot(position, velocity, 100)
                   for position, velocity in zip(positions, velocities)]
quadrant_counts = count_by_quadrant(final_positions)

res = quadrant_counts[0] * quadrant_counts[1] * \
    quadrant_counts[2] * quadrant_counts[3]
print(res)

# * Part 2

# ! IDEA: find the first step where robots are creating a tree shape
# ! we can reduce computation by checking only the line where we have at least 30 robots aligned
# ! we can find the line by counting the number of robots in each line

res = find_easter_egg(positions, velocities)
print(res)
