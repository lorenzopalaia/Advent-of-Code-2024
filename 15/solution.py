with open("15/data.txt", "r") as f:
    grid_data, move_data = f.read().strip().split("\n\n")

DIR_MAP = {
    "^": 1j,  # Up
    ">": 1,   # Right
    "v": -1j,  # Down
    "<": -1,  # Left
}


def parse_grid(raw):
    start_position = None
    grid = {}
    for y, row in enumerate(raw.split("\n")):
        for x, char in enumerate(row):
            position = complex(x, -y)
            grid[position] = char
            if char == "@":
                start_position = position
                grid[start_position] = "."
    return start_position, grid


def parse_moves(raw):
    return [DIR_MAP[direction] for direction in raw if direction in DIR_MAP]


def robot_move(start, moves, grid):
    robot = start
    for move in moves:
        target = robot + move
        if grid.get(target) == ".":
            robot = target
        elif grid.get(target) == "#":
            continue
        else:
            step = 1
            while grid.get(robot + step * move, "#") not in ".#":
                step += 1
            final_target = robot + step * move
            if grid.get(final_target) == ".":
                grid[final_target] = "O"
                grid[target] = "."
                robot = target


def gps(position):
    return int(-100 * position.imag + position.real)


# * Part 1
robot_start, grid = parse_grid(grid_data)
moves = parse_moves(move_data)

robot_move(robot_start, moves, grid)

res = sum(gps(pos) for pos, item in grid.items() if item == "O")
print(res)
