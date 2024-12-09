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
  while disk_map[position] >= 0:
    position += 1
  return position

def find_previous_occupied_position(disk_map, position):
  while disk_map[position] < 0:
    position -= 1
  return position

# * Part 1
def defragment_disk(disk_map):
  first_free_position = find_next_free_position(disk_map, 0)
  last_occupied_position = find_previous_occupied_position(disk_map, len(disk_map) - 1)

  while last_occupied_position > first_free_position:
    disk_map[first_free_position] = disk_map[last_occupied_position]
    first_free_position = find_next_free_position(disk_map, first_free_position + 1)
    last_occupied_position = find_previous_occupied_position(disk_map, last_occupied_position - 1)

  return sum(index * disk_map[index] for index in range(last_occupied_position + 1))

res = defragment_disk(disk_map[:])
print(res)