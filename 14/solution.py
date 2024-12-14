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


# * Part 1
final_positions = [simulate_robot(position, velocity, 100)
                   for position, velocity in zip(positions, velocities)]
quadrant_counts = count_by_quadrant(final_positions)

res = quadrant_counts[0] * quadrant_counts[1] * \
    quadrant_counts[2] * quadrant_counts[3]
print(res)
