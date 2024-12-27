with open("10/data.txt", "r") as file:
  data = file.read().strip().split("\n")

n = len(data)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def is_inbound(i, j):
  return 0 <= i < n and 0 <= j < n

# * Part 1

# ! IDEA: run a DFS from each cell with a 0, and count the number of paths that reach the end
# ! If the path reaches the end, increment the total score
# ! Use a stack to keep track of the current cell, and a set to keep track of visited cells

def get_score(i, j):
  if data[i][j] != "0":
    return 0

  tot = 0

  stack = [(i, j)]
  visited = set()

  while len(stack) > 0:
    ptr_i, ptr_j = stack.pop()
    ptr = int(data[ptr_i][ptr_j])    

    if ptr == 9:
      tot += 1      
      continue

    for di, dj in directions:
      next_i, next_j = ptr_i + di, ptr_j + dj

      if not is_inbound(next_i, next_j):        
        continue

      next = int(data[next_i][next_j])

      if next != ptr + 1:        
        continue

      if (next_i, next_j) in visited:        
        continue
      
      stack.append((next_i, next_j))
      visited.add((next_i, next_j))

  return tot

tot = 0
for i in range(n):
  for j in range(n):    
    tot += get_score(i, j)

print(tot)

# * Part 2

# ! IDEA: use a recursive approach to count the paths
# ! Starting from each 0, recursively calculate the rating of each cell
# ! The rating of a cell is the sum of the ratings of the subsequent cells (+1)
# ! A cell with 9 has a rating of 1, being the endpoint

def get_rating(i, j):
  if data[i][j] == "9":
    return 1
  
  tot = 0
  for di, dj in directions:
    next_i, next_j = i + di, j + dj

    if not is_inbound(next_i, next_j):
      continue
  
    if int(data[next_i][next_j]) == int(data[i][j]) + 1:
      tot += get_rating(next_i, next_j)

  return tot

tot = 0
for i in range(n):
  for j in range(n):
    if data[i][j] == "0":
      tot += get_rating(i, j)

print(tot)