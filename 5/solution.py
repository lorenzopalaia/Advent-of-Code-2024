with open("5/rules.txt", "r") as file:
  rules = file.read().splitlines()

rules = [list(map(int, rule.split("|"))) for rule in rules]

with open("5/orders.txt", "r") as file:
  orders = file.read().splitlines()

orders = [list(map(int, order.split(","))) for order in orders]

# * Part 1

# Create a dictionary with the dependencies where the key is the first element and the value is a list of the second elements
dependencies = {}
for rule in rules:
  if rule[0] not in dependencies:
    dependencies[rule[0]] = []  
  dependencies[rule[0]].append(rule[1])  

def check_order(order, dependencies):
  for i in range(len(order)):
    for j in range(i+1, len(order)):      
      if order[j] in dependencies and order[i] in dependencies[order[j]]:
        return False
  return True

res = 0

for order in orders:
  if check_order(order, dependencies):    
    res += order[len(order)//2]

print(res)

# * Part 2

# Filter the invalid orders
invalid_orders = [order for order in orders if not check_order(order, dependencies)]

def reorder(order, dependencies):
  for i in range(len(order)):
    for j in range(i+1, len(order)):      
      if order[j] in dependencies and order[i] in dependencies[order[j]]:
        # Swap the elements
        order[i], order[j] = order[j], order[i]
  return order

invalid_orders = [reorder(order, dependencies) for order in invalid_orders]

res = 0

for order in invalid_orders:
  res += order[len(order)//2]

print(res)