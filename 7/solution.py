from itertools import product

with open("7/data.txt", "r") as file:
  data = file.read().splitlines()

equations = []
for line in data:
  key, value = line.split(':')
  equations.append({
    "key": int(key),
    "value": [int(x) for x in value.strip().split()]
  })

# * Function to solve the equation
def solve_equation(key, values, operator_types):
  operator_positions = len(values) - 1
  for operators in product(range(operator_types), repeat=operator_positions):
    result = values[0]
    for i, op in enumerate(operators):
      if op == 0:  # Sum
        result += values[i + 1]
      elif op == 1:  # Multiplication
        result *= values[i + 1]
      elif op == 2:  # Concatenation
        result = int(str(result) + str(values[i + 1]))
    if result == key:
      return key
  return 0

# * Part 1
res = sum(solve_equation(eq["key"], eq["value"], 2) for eq in equations)
print(res)

# * Part 2
res = sum(solve_equation(eq["key"], eq["value"], 3) for eq in equations)
print(res)
