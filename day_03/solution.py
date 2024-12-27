with open("3/data.txt") as f:
  data = f.read()

# Part 1

import re
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(mul_pattern, data)

res = sum([int(a) * int(b) for a, b in matches])

print(res)

# Part 2

dont_pattern = r"don't\(\)"
dont_matches = re.findall(dont_pattern, data)
dont_indices = [match.start() for match in re.finditer(dont_pattern, data)]

do_pattern = r"do\(\)"
do_matches = re.findall(do_pattern, data)
do_indices = [match.start() for match in re.finditer(do_pattern, data)]

# * IDEA: extract the substring within each "do()" and "don't()" block
# * Find all matches of the mul() pattern within each "do()" block
# * Sum the products of the matches within each "do()" block
# * Remove "do()" indices that are within the current "don't()" block, in case there are nested "do()" blocks
# * Make it work like a stack, where we process the very first "do()" block first

# Add a starting point at the beginning of the data
do_indices.insert(0, 0)

res = 0

while do_indices:
  start = do_indices.pop(0)
  end = min([x for x in dont_indices if x > start] or [len(data)])
 
  substring = data[start:end]
  matches = re.findall(mul_pattern, substring)

  res += sum([int(a) * int(b) for a, b in matches])

  do_indices = [x for x in do_indices if x > end]

print(res)