#!/usr/bin/env python3

with open('2/data.txt') as f:
  input_list = [list(map(int, line.strip().split())) for line in f]


# Part 1
safe = 0

def is_increasing(level):
  for i in range(len(level) - 1):
    if level[i] < level[i + 1]:
      continue
    else:
      return False
  return True

def is_decreasing(level):
  for i in range(len(level) - 1):
    if level[i] > level[i + 1]:
      continue
    else:
      return False
  return True

def is_between_1_and_3(level):
  for i in range(len(level) - 1):
    if abs(level[i + 1] - level[i]) >= 1 and abs(level[i + 1] - level[i]) <= 3:
      continue
    else:
      return False
  return True

def is_safe(level):
  if (is_increasing(level) or is_decreasing(level)) and is_between_1_and_3(level):
    return True
  return False

for level in input_list:
  if is_safe(level):
    safe += 1

print(safe)

# Part 2