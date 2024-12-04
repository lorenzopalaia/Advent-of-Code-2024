data = []

with open('4/data.txt', 'r') as f:
    for line in f.readlines():
        data.append(list(line.strip()))
n = len(data)

def is_inbounds(i, j):
    return 0 <= i < n and 0 <= j < n

# * Part 1
res = 0

for i in range(n):
  for j in range(n):
    # skip if not X, since X is the first letter of XMAS
    if data[i][j] != 'X':
      continue
    # check all 8 directions arond (i, j) using (di, dj), where (0, 1) is right, (1, 0) is down, etc.
    for di in [-1, 0, 1]:
      for dj in [-1, 0, 1]:
        # skip if (di, dj) is (0, 0) since it is the center
        if (di, dj) == (0, 0):
          continue
        # if there's enough space to form XMAS, check if it is XMAS
        if is_inbounds(i + 3 * di, j + 3 * dj):
          string = ''.join(data[i + k * di][j + k * dj] for k in range(4))
          if string == 'XMAS':
            res += 1

print(res)

# * Part 2
def is_valid_square(data, i, j):
  # skip if center is not A    
  if data[i][j] != "A":
    return False
  # define the 4 corners of the square
  square = [data[i - 1][j - 1], data[i - 1][j + 1], data[i + 1][j - 1], data[i + 1][j + 1]]
  return (
    (square[0] == "M" and square[1] == "M" and square[2] == "S" and square[3] == "S")
    or (square[0] == "S" and square[1] == "S" and square[2] == "M" and square[3] == "M")
    or (square[0] == "M" and square[1] == "S" and square[2] == "M" and square[3] == "S")
    or (square[0] == "S" and square[1] == "M" and square[2] == "S" and square[3] == "M")
  )

res = 0

for i in range(1, len(data) - 1):
  for j in range(1, len(data[i]) - 1):
    if is_valid_square(data, i, j):
      res += 1

print(res)