with open('13/data.txt') as f:
    lines = [line.rstrip() for line in f]

# ! IDEA: Use Cramer's Rule to solve the system of linear equations
# ! Cramer's Rule:
# ! a1x + b1y = c1
# ! a2x + b2y = c2
# ! x = (c1b2 - c2b1) / (a1b2 - a2b1)
# ! y = (a1c2 - a2c1) / (a1b2 - a2b1)


def solve(part):
    total_tokens = 0
    add = 10000000000000 if part == 2 else 0

    for line in lines:
        if line.startswith("Button"):
            parts = line.split(" ")
            button = parts[1].split(":")[0]
            if button == 'A':
                x1 = int(parts[2][2:-1])
                y1 = int(parts[3][2:])
            else:
                x2 = int(parts[2][2:-1])
                y2 = int(parts[3][2:])

        elif line.startswith("Prize"):
            parts = line.split(" ")
            prize_x = int(parts[1][2:-1]) + add
            prize_y = int(parts[2][2:]) + add

            a = (prize_x * y2 - prize_y * x2) / (x1 * y2 - y1 * x2)
            b = (prize_y * x1 - prize_x * y1) / (x1 * y2 - y1 * x2)
            if a == int(a) and b == int(b):
                total_tokens += int(3 * a + b)

    return total_tokens


# * Part 1
res = solve(1)
print(res)

# * Part 2
res = solve(2)
print(res)
