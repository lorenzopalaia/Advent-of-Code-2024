with open("9/data.txt", "r") as file:
  data = file.read().strip()

disk_map = []
occupied_areas = []
free_areas = []

# Parse the input and populate the disk map, occupied, and free areas
for index in range(0, len(data), 2):
  area_size = int(data[index])
  occupied_areas.append((len(disk_map), area_size))
  disk_map += [index // 2] * area_size
  if index + 1 < len(data):
    area_size = int(data[index + 1])
    if area_size > 0:
      free_areas.append([len(disk_map), area_size])
      disk_map += [-1] * area_size

# * Helper Functions
def find_next_free_position(disk_map, position):
  # Find the next free position in the disk map
  while disk_map[position] >= 0:
    position += 1
  return position

def find_previous_occupied_position(disk_map, position):
  # Find the previous occupied position in the disk map
  while disk_map[position] < 0:
    position -= 1
  return position

# * Part 1
def defragment_disk_part1(disk_map):
  first_free_position = find_next_free_position(disk_map, 0)
  last_occupied_position = find_previous_occupied_position(disk_map, len(disk_map) - 1)

  while last_occupied_position > first_free_position:
    # Move the last occupied block to the first free position
    disk_map[first_free_position] = disk_map[last_occupied_position]
    first_free_position = find_next_free_position(disk_map, first_free_position + 1)
    last_occupied_position = find_previous_occupied_position(disk_map, last_occupied_position - 1)

  return sum(index * disk_map[index] for index in range(last_occupied_position + 1))

res = defragment_disk_part1(disk_map[:])
print(res)

# * Part 2
def find_first_suitable_free_area(free_areas, required_size):
  # Find the first free area that is large enough to accommodate the required size
  for index, free_area in enumerate(free_areas):
    if free_area[1] >= required_size:
      return index, free_area
  return None, None

def defragment_disk_part2(disk_map):
  for occupied_area in occupied_areas[::-1]:
    occupied_area_size = occupied_area[1]
    free_area_index, free_area = find_first_suitable_free_area(free_areas, occupied_area_size)

    if free_area and free_area[0] < occupied_area[0]:
      block_id = disk_map[occupied_area[0]]
      # Move the occupied block to the free area
      for i in range(occupied_area_size):
        disk_map[free_area[0] + i] = block_id
        disk_map[occupied_area[0] + i] = -1

      # Update the free areas list
      if free_areas[free_area_index][1] > occupied_area_size:
        free_areas[free_area_index][0] += occupied_area_size
        free_areas[free_area_index][1] -= occupied_area_size
      else:
        free_areas.pop(free_area_index)

  return sum(index * disk_map[index] for index in range(len(disk_map)) if disk_map[index] > 0)

res = defragment_disk_part2(disk_map[:])
print(res)
