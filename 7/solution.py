with open("7/data.txt", "r") as file:
  data = file.read().splitlines()

equations = []
for line in data:  
  # key, value = line.split(':')
  # equations[int(key)] = [int(x) for x in value.strip().split(' ')]
  key, value = line.split(':')
  equations.append({
    "key": int(key),
    "value" : [int(x) for x in value.strip().split(' ')]
  })

# * Part 1

res = 0

# TODO: optimize

for equation in equations:
  # calculate the number of operator positions
  operator_positions = len(equation["value"]) - 1
  # there are 2^operator_positions possible combinations of operators
  for i in range(2**operator_positions):
    operators = []
    temp = i
    for _ in range(operator_positions):
      # determine if the operator is + (0) or * (1)
      operators.append(temp % 2)
      temp //= 2
    result = equation["value"][0]
    for j in range(operator_positions):
      # apply the sum
      if operators[j] == 0:
        result += equation["value"][j+1]
      # apply the multiplication
      else:
        result *= equation["value"][j+1]
    if result == equation["key"]:
      res += equation["key"]
      break

print(res)