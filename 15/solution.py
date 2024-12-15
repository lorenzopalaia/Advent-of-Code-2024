with open("15/data.txt", "r") as f:
    grid_data, move_data = f.read().strip().split("\n\n")

DIR_MAP = {
    "^": 1j,  # Up
    ">": 1,   # Right
    "v": -1j,  # Down
    "<": -1,  # Left
}


def parse_grid(raw, is_part_two=False):
    start = 0
    grid = {}
    for i, row in enumerate(raw.split("\n")):
        for r, char in enumerate(row):
            if is_part_two:
                if char in ".#":
                    grid[complex(2 * r, -i)] = char
                    grid[complex(2 * r + 1, -i)] = char
                elif char == "O":
                    grid[complex(2 * r, -i)] = "["
                    grid[complex(2 * r + 1, -i)] = "]"
                else:
                    grid[complex(2 * r, -i)] = "."
                    grid[complex(2 * r + 1, -i)] = "."
                    start = complex(2 * r, -i)
            else:
                grid[complex(r, -i)] = char
                if char == "@":
                    start = complex(r, -i)
                    grid[start] = "."
    return start, grid


def parse_moves(raw):
    return [DIR_MAP[direction] for direction in raw if direction != "\n"]


def can_move_vert(pos, direction, grid):
    if grid[pos] == "]":
        delta = -1
    elif grid[pos] == "[":
        delta = 1
    else:
        return grid[pos] == "."
    if grid[pos + direction] == "." and grid[pos + direction + delta] == ".":
        return True
    if grid[pos + direction] == "#" or grid[pos + direction + delta] == "#":
        return False
    return can_move_vert(pos + direction, direction, grid) and can_move_vert(pos + direction + delta, direction, grid)


def move_vert(pos, direction, grid):
    if grid[pos] == "]":
        delta = -1
    elif grid[pos] == "[":
        delta = 1
    else:
        return None
    while grid[pos + direction] != "." or grid[pos + direction + delta] != ".":
        move_vert(pos + direction, direction, grid)
        move_vert(pos + direction + delta, direction, grid)
    grid[pos + direction] = grid[pos]
    grid[pos + direction + delta] = grid[pos + delta]
    grid[pos] = "."
    grid[pos + delta] = "."


def can_move_horiz(pos, direction, grid):
    char = grid[pos + 2 * direction]
    if char == "#":
        return False
    if char == ".":
        return True
    else:
        return can_move_horiz(pos + 2 * direction, direction, grid)


def move_horiz(pos, direction, grid):
    while grid[pos + 2 * direction] != ".":
        move_horiz(pos + 2 * direction, direction, grid)
    grid[pos + 2 * direction] = grid[pos + direction]
    grid[pos + direction] = grid[pos]
    grid[pos] = "."


def robot_move(robot, moves, grid, is_part_two=False):
    for move in moves:
        if grid[robot + move] == ".":
            robot += move
        elif grid[robot + move] == "#":
            continue
        else:
            nb = 1
            if not is_part_two:
                while grid[robot + nb * move] not in ".#":
                    nb += 1
                if grid[robot + nb * move] == "#":
                    continue
                else:
                    grid[robot + nb * move] = "O"
                    grid[robot + move] = "."
                    robot += move
            else:
                if move in (1, -1):
                    if not can_move_horiz(robot + move, move, grid):
                        continue
                    move_horiz(robot + move, move, grid)
                elif not can_move_vert(robot + move, move, grid):
                    continue
                else:
                    move_vert(robot + move, move, grid)
                robot += move


def gps(c):
    return int(-100 * c.imag + c.real)


moves = parse_moves(move_data)

# * Part 1

# ! IDEA:
# ! Every time the robot moves, it checks if there is a box ("O") in front of it. If there is,
# ! the robot will attempt to move the box in its path. If there are obstacles ("#"), neither
# ! the robot nor the box will move. The goal is to calculate the sum of the GPS coordinates
# ! (summing the result of -100 * position_y + position_x) for all boxes ("O") that are
# ! located at the robot's final position.

robot_start, grid = parse_grid(grid_data, is_part_two=False)

robot_move(robot_start, moves, grid, is_part_two=False)

res = sum(gps(pos) for pos, item in grid.items() if item == "O")
print(res)

# * Part 2

# ! IDEA:
# ! The key difference from Part 1 is that now the robot must also move in a more complex way, using
# ! the can_move_horiz and can_move_vert functions to check if it's possible to move boxes
# ! based on position and direction. The robot can move boxes both horizontally and vertically, but it
# ! cannot do so if there are obstacles (walls). Once the robot has moved, we calculate the sum of GPS
# ! coordinates for all boxes ("[") that are located at the robot's final position.

robot_start, grid = parse_grid(grid_data, is_part_two=True)

robot_move(robot_start, moves, grid, is_part_two=True)

res = sum(gps(pos) for pos, item in grid.items() if item == "[")
print(res)
