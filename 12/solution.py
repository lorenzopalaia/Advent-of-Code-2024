with open("12/data.txt", "r") as file:
  data = file.read().splitlines()

# ! IDEA: Identify distinct regions of the same plot type.
# ! Use search algorithms like DFS or BFS to find all connected regions.
# ! For each region, calculate its area (number of cells) and its perimeter (number of outer edges).
# ! Finally, calculate the price for each region by multiplying its area by its perimeter and summing the results.

def is_inbound(data, i, j):
  return i >= 0 and i < len(data) and j >= 0 and j < len(data[i])

def expand_region(data, visited, i, j, region=None):
  if region is None:
    region = set()
  
  region.add((i, j))
  visited.add((i, j))

  for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):    
    next_i, next_j = i + di, j + dj
    if is_inbound(data, next_i, next_j):
      plot = data[i][j]
      neighbor_plot = data[next_i][next_j]
      if plot == neighbor_plot and (next_i, next_j) not in visited:
        expand_region(data, visited, next_i, next_j, region)

  return region

def find_regions(data):
  visited = set()
  regions = []
  for i, row in enumerate(data):
    for j, plot in enumerate(row):
      if (i, j) in visited:
        continue
      region = expand_region(data, visited, i, j)
      regions.append(region)
  return regions

def calc_perimeter(region):
  perimeter = 0
  for i, j in region:
    perimeter += 4
    
    up_i, up_j = i - 1, j
    if (up_i, up_j) in region:
      perimeter -= 2

    left_i, left_j = i, j - 1
    if (left_i, left_j) in region:
      perimeter -= 2

  return perimeter

def calc_area(region):
  return len(region)

def calc_price(region):
  return calc_area(region) * calc_perimeter(region)

# * Part 1
regions = find_regions(data)
total_price = sum(calc_price(region) for region in regions)
print(total_price)