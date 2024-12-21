from functools import cache

with open("21/data.txt", "r") as file:
    codes = [line.rstrip("\n") for line in file]

GAP = "X"
NUMERIC_KEYPAD = ["789", "456", "123", "X0A"]
DIRECTIONAL_KEYPAD = ["X^A", "<v>"]


def locate_key(key, keypad):
    for row_index, row in enumerate(keypad):
        for col_index, char in enumerate(row):
            if char == key:
                return row_index, col_index


def shortest_path(key1, key2, keypad):
    row1, col1 = locate_key(key1, keypad)
    row2, col2 = locate_key(key2, keypad)
    dr, dc = row2 - row1, col2 - col1

    row_moves = "v" * dr if dr >= 0 else "^" * (-dr)
    col_moves = ">" * dc if dc >= 0 else "<" * (-dc)

    if dr == dc == 0:
        return [""]
    elif dr == 0:
        return [col_moves]
    elif dc == 0:
        return [row_moves]
    elif keypad[row1][col2] == GAP:
        return [row_moves + col_moves]
    elif keypad[row2][col1] == GAP:
        return [col_moves + row_moves]
    else:
        return [row_moves + col_moves, col_moves + row_moves]


@cache
def calculate_presses(sequence, depth):
    if depth == 1:
        return len(sequence)

    if any(c in sequence for c in "012345679"):
        keypad = NUMERIC_KEYPAD
    else:
        keypad = DIRECTIONAL_KEYPAD

    total_presses = 0
    for key1, key2 in zip("A" + sequence, sequence):
        paths = shortest_path(key1, key2, keypad)
        total_presses += min(calculate_presses(path + "A", depth - 1)
                             for path in paths)
    return total_presses


def compute_complexity(code, num_keypads):
    return calculate_presses(code, num_keypads) * int(code[:3])

# ! IDEA: We can use a recursive function to calculate the minimum number of presses
# ! required to type a given code.


# * Part 1
res = sum(compute_complexity(code, 1 + 2 + 1) for code in codes)
print(res)

# * Part 2
res = sum(compute_complexity(code, 1 + 25 + 1) for code in codes)
print(res)
