with open('13/data.txt') as f:
    lines = [line.rstrip() for line in f]

# ! IDEA: Use Cramer's Rule to solve the system of linear equations
# !
# ! Cramer's Rule:
# ! a_1 x + b_1 y = c_1
# ! a_2 x + b_2 y = c_2
# ! x = (c_1 b_2 - c_2 b_1) / (a_1 b_2 - a_2 b_1)
# ! y = (a_1 c_2 - a_2 c_1) / (a_1 b_2 - a_2 b_1)
# !
# ! Each combination of Button and Prize is a system of linear equations based on the coordinates x and y
# !
# ! Equations are:
# ! a * (x_1 + offset_1) + b * (y_1 + offset_1) = prize_x + add
# ! a * (x_2 + offset_2) + b * (y_2 + offset_2) = prize_y + add
# ! Where:
# ! (x_1, y_1) and (x_2, y_2) are the coefficients of a and b for the Buttons A and B
# ! offset_1 and offset_2 are the increments to the coordinates of the Buttons A and B
# ! (prize_x, prize_y) are the coordinates of the Prize
# ! add is 10000000000000 for Part 2 and 0 for Part 1


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
                #  A button costs 3 tokens and B button costs 1 token
                total_tokens += int(3 * a + b)

    return total_tokens


# * Part 1
res = solve(1)
print(res)

# * Part 2
res = solve(2)
print(res)
