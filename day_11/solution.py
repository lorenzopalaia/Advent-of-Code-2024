from collections import defaultdict

with open("11/data.txt") as f:
  input_data = f.read()

# ! IDEA: Instead of tracking actual numbers, we'll track patterns that lead to stone multiplication
# ! 
# ! Instead of maintaining a list of actual stones and modifying them (which requires memory and 
# ! computational overhead for insertions and modifications), we track:
# ! 1. The number itself
# ! 2. Its "age" (how many transformations it's been through)
# ! 3. How many instances of each unique number+age combination exist
# !
# ! For example, instead of storing ['1', '1', '2', '2'] as a list,
# ! we store it as a dictionary: {('1',age): 2, ('2',age): 2} 
# ! This drastically reduces memory usage and computational complexity since we're
# ! just updating counts instead of manipulating a list of strings.

def count_stones_after_blinks(initial_data, blinks):
  stone_patterns = defaultdict(int)

  # Initialize with input data
  for num in initial_data:
    stone_patterns[(num, 0)] += 1

  def process_number(num, age):
    if num == "0":
      return [("1", age + 1)]

    # Even number of digits - splits into two
    if len(num) % 2 == 0:
      mid = len(num) // 2
      left = num[:mid].lstrip("0") or "0"
      right = num[mid:].lstrip("0") or "0"
      return [(left, age + 1), (right, age + 1)]

    # Multiply by 2024
    result = str(int(num) * 2024)
    return [(result, age + 1)]

  for current_blink in range(blinks):
    new_patterns = defaultdict(int)

    for (num, age), count in stone_patterns.items():
      results = process_number(num, age)
      for new_num, new_age in results:
        new_patterns[(new_num, new_age)] += count

    stone_patterns = new_patterns

    # ! Optimization: If we're only interested in the count, we can periodically
    # ! reset the age counter to prevent tuple explosion
    if current_blink % 10 == 9:  # Every 10 iterations
      cleaned_patterns = defaultdict(int)
      for (num, _), count in stone_patterns.items():
        cleaned_patterns[(num, 0)] += count
      stone_patterns = cleaned_patterns

  return sum(stone_patterns.values())

def solve(input_data, blinks=25):
  data = input_data.strip().split()
  return count_stones_after_blinks(data, blinks)

# * Part 1
res = solve(input_data, 25)
print(res)

# * Part 2
res = solve(input_data, 75)
print(res)