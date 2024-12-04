with open("4/data.txt") as f:
  data = f.read().splitlines()

import re

# Part 1
pattern = r"XMAS"

res = 0

horizontal = [list(x) for x in data]

def count_line(data):
  count = 0

  for i in range(len(data)):
    for j in range(len(data[i]) - 3):
      word = "".join(data[i][j:j+4])
      if re.match(pattern, word):
        count += 1

  return count

res += count_line(horizontal)

# vertical
vertical = list(map(list, zip(*data)))

res += count_line(vertical)

# horizontal reversed
horizontal_reversed = [list(reversed(x)) for x in data]

res += count_line(horizontal_reversed)

# vertical reversed
vertical_reversed = [list(reversed(x)) for x in vertical]

res += count_line(vertical_reversed)

# diagonal to left
diagonal_to_left = []
for i in range(len(data)):
  for j in range(len(data[i])):
    if i + 3 < len(data) and j + 3 < len(data[i]):
      diagonal_to_left.append([data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]])

res += count_line(diagonal_to_left)

# diagonal to right
diagonal_to_right = []
for i in range(len(data)):
  for j in range(len(data[i])):
    if i + 3 < len(data) and j - 3 >= 0:
      diagonal_to_right.append([data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]])

res += count_line(diagonal_to_right)

# diagonal to left reversed
diagonal_to_left_reversed = [list(reversed(x)) for x in diagonal_to_left]

res += count_line(diagonal_to_left_reversed)

# diagonal to right reversed
diagonal_to_right_reversed = [list(reversed(x)) for x in diagonal_to_right]

res += count_line(diagonal_to_right_reversed)

print(res)

# Part 2

def is_valid_square(data, i, j):
    # skip if center is not A    
    if data[i][j] != "A":
      return False
    square = [data[i - 1][j - 1], data[i - 1][j + 1], data[i + 1][j - 1], data[i + 1][j + 1]]
    return (
      (square[0] == "M" and square[1] == "M" and square[2] == "S" and square[3] == "S")
      or (square[0] == "S" and square[1] == "S" and square[2] == "M" and square[3] == "M")
      or (square[0] == "M" and square[1] == "S" and square[2] == "M" and square[3] == "S")
      or (square[0] == "S" and square[1] == "M" and square[2] == "S" and square[3] == "M")
    )

# Conta i quadrati validi
res = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if is_valid_square(data, i, j):
            res += 1

print(res)