with open('13/data.txt') as f:
    lines = [line.rstrip() for line in f]

# ! IDEA: Use Cramer's Rule to solve the system of linear equations
# ! Cramer's Rule:
# ! a1x + b1y = c1
# ! a2x + b2y = c2
# ! x = (c1b2 - c2b1) / (a1b2 - a2b1)
# ! y = (a1c2 - a2c1) / (a1b2 - a2b1)

# * Part 1


def solve_part1():
    total_tokens = 0
    for line in lines:
        if line.startswith("Button"):
            parts = line.split(" ")
            button = parts[1].split(":")[0]
            if button == 'A':
                button_a_x = int(parts[2][2:-1])
                button_a_y = int(parts[3][2:])
            else:
                button_b_x = int(parts[2][2:-1])
                button_b_y = int(parts[3][2:])

        elif line.startswith("Prize"):
            parts = line.split(" ")
            prize_x = int(parts[1][2:-1])
            prize_y = int(parts[2][2:])
            a = (prize_x * button_b_y - prize_y * button_b_x) / \
                (button_a_x * button_b_y - button_a_y * button_b_x)
            b = (prize_y * button_a_x - prize_x * button_a_y) / \
                (button_a_x * button_b_y - button_a_y * button_b_x)
            if a == int(a) and b == int(b):
                total_tokens += int(3 * a + b)

    print(total_tokens)


solve_part1()
