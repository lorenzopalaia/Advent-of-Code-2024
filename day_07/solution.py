import re

with open("7/data.txt", "r") as f:
  data = [list(map(int, re.findall('\d+', row))) for row in f]

# ! IDEA: Use a set to store intermediate subtotals
# * 1. Iterate over the numbers in reverse order,
#      as we need to "resolve" the target backward starting from each number.
# * 2. For each number, determine how the current subtotal could have been produced
#      using addition, multiplication, or concatenation (in Part 2).
#      Each possible intermediate result is added to the new set of subtotals.
# 
# ** Explanation of operations:
# - If the subtotal `sub` is divisible by the current number, it is possible that the result 
#   was produced by multiplication. Therefore, we add the quotient (`sub // number`) to the new subtotals.
# 
# - If the subtotal `sub` is greater than or equal to the current number, it is possible that the result 
#   was produced by inverse subtraction (forward addition). Hence, we add the result of the difference 
#   (`sub - number`) to the new subtotals.
# 
# - **For Part 2:** If `sub` ends with the current number (as a string), it is possible that the number 
#   was "removed" through concatenation. In this case, we remove the trailing part of the subtotal and 
#   add the result to the new set of subtotals.
# 
# ** Iteration:
# - Update `subtotals` with the newly computed values.
# - At the end, check if the original target can be reduced to zero using the described rules.
#   If yes, the equation is valid for that target, and we return the target value; otherwise, we return False.


# * Function to solve the equation
def solve_equation(target, numbers, is_part2):
  # Initialize a set with the target value
  subtotals = {target}  
  for number in reversed(numbers):
    new_sub = set()    
    for sub in subtotals:
      # If sub is divisible by number, add the quotient to new_sub
      if not sub % number:
        new_sub.add(sub // number)
      # If sub is greater than or equal to number, add the difference to new_sub
      if sub >= number:
        new_sub.add(sub - number)
      # * Skip the rest if not part 2
      if not is_part2:
        continue
      # * Additional condition for part 2: if sub ends with number
      str_sub, str_num = map(str, [sub, number])
      if sub > number and str_sub.endswith(str_num):
        new_sub.add(int(str_sub[:-len(str_num)]))
    # Update subtotals
    subtotals = new_sub
  # Return target if 0 is in subtotals, otherwise return False
  return target if 0 in subtotals else False

def solve(p):
  part1 = part2 = 0
  for target, *numbers in p:    
    part1 += solve_equation(target, numbers, is_part2=False)
    part2 += solve_equation(target, numbers, is_part2=True)  
  return part1, part2

sol = solve(data)

# * Part 1
print(sol[0])

# * Part 2
print(sol[1])