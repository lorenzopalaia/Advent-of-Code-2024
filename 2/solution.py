#!/usr/bin/env python3

with open('2/data.txt') as f:
  input_list = [list(map(int, line.strip().split())) for line in f]

# Part 1
def is_increasing(report):
  for i in range(len(report) - 1):
    if report[i] < report[i + 1]:
      continue
    else:
      return False
  return True

def is_decreasing(report):
  for i in range(len(report) - 1):
    if report[i] > report[i + 1]:
      continue
    else:
      return False
  return True

def is_between_1_and_3(report):
  for i in range(len(report) - 1):
    if abs(report[i + 1] - report[i]) >= 1 and abs(report[i + 1] - report[i]) <= 3:
      continue
    else:
      return False
  return True

def is_safe(report):
  if (is_increasing(report) or is_decreasing(report)) and is_between_1_and_3(report):
    return True
  return False

safe = 0

for report in input_list:
  if is_safe(report):
    safe += 1

print(safe)

# Part 2
def is_monotonic_and_in_range(levels):
  diffs = []
  for a, b in zip(levels, levels[1:]):
    diffs.append(a - b)
  
  is_monotonic = True
  for i in diffs:
    if i <= 0:
      is_monotonic = False
      break
  if not is_monotonic:
    is_monotonic = True
    for i in diffs:
      if i >= 0:
        is_monotonic = False
        break

  is_in_range = True
  for i in diffs:
    if abs(i) < 1 or abs(i) > 3:
      is_in_range = False
      break

  if is_monotonic and is_in_range:
    return True
  return False

safe = 0

for report in input_list:
  levels = report
  if is_monotonic_and_in_range(levels):
    safe += 1
  else:
    for i in range(len(levels)):
      tolerated_levels = levels[:i] + levels[i + 1:]
      if is_monotonic_and_in_range(tolerated_levels):
        safe += 1
        break

print(safe)