with open("12/data.txt", "r") as file:
  data = file.read().splitlines()

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

def calc_sides(region, visited=None, i=None, j=None):
  if visited is None:
    visited = set()
    i, j = min(region)

  if (i, j) in visited or (i, j) not in region:
    return 0
  visited.add((i, j))

  vertical_sides = {(0, 1), (0, -1)}
  horizontal_sides = {(1, 0), (-1, 0)}
  total_sides = vertical_sides.union(horizontal_sides)

  sides = set()
  for side in total_sides:
    di, dj = side
    next_i, next_j = i + di, j + dj

    if (next_i, next_j) not in region:
      sides.add(side)

  vertical_sides = vertical_sides.intersection(sides)
  horizontal_sides = horizontal_sides.intersection(sides)

  sides_count = 0

  for side in vertical_sides:
    di, dj = side
    upper_i, upper_j = i - 1, j
    if (upper_i, upper_j) not in region:
      sides_count += 1
    else:
      upper_side_i, upper_side_j = upper_i + di, upper_j + dj
      if (upper_side_i, upper_side_j) in region:
        sides_count += 1

  for side in horizontal_sides:
    di, dj = side
    left_i, left_j = i, j - 1
    if (left_i, left_j) not in region:
      sides_count += 1
    else:
      left_side_i, left_side_j = left_i + di, left_j + dj
      if (left_side_i, left_side_j) in region:
        sides_count += 1

  for di, dj in total_sides:
    next_i, next_j = i + di, j + dj
    sides_count += calc_sides(region, visited, next_i, next_j)

  return sides_count

regions = find_regions(data)

# * Part 1

# ! IDEA: Identify distinct regions of the same plot type.
# ! Use search algorithms like DFS or BFS to find all connected regions.
# ! For each region, calculate its area (number of cells) and its perimeter (number of outer edges).
# ! Finally, calculate the price for each region by multiplying its area by its perimeter and summing the results.

total_price = sum(calc_area(region) * calc_perimeter(region) for region in regions)
print(total_price)

# * Part 2

# ! IDEA: Calculate the unique sides for each region.
# ! For each cell in the region, count the sides that are borders of the region.
# ! Ensure that sides are counted only once by checking neighbors.
# ! Sum the unique sides for each region and multiply by the area of the region.
# ! Finally, sum the results for all regions.

res = sum(calc_sides(region) * calc_area(region) for region in regions)
print(res)
