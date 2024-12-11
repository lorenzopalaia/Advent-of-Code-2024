with open("11/data.txt", "r") as file:
  data = file.read().strip().split(" ")

# * Part 1

def process_data(data):
  i = 0
  while i < len(data):
    if data[i] == "0":
      data[i] = "1"
    elif len(data[i]) % 2 == 0:
      first_half = data[i][:len(data[i]) // 2].lstrip("0")
      second_half = data[i][len(data[i]) // 2:].lstrip("0")
      data[i] = first_half if first_half else "0"
      data.insert(i + 1, second_half if second_half else "0")
      i += 1  # Skip the next element
    else:
      data[i] = str(int(data[i]) * 2024)
    i += 1
  return data

for blink in range(25):
  data = process_data(data)
  
res = len(data)
print(res)