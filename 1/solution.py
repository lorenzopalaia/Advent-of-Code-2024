from collections import Counter


with open('1/data.txt') as f:
    input_list = [list(map(int, line.strip().split())) for line in f]

left_list = []
right_list = []
for i in range(len(input_list)):
    left_list.append(input_list[i][0])
    right_list.append(input_list[i][1])

# Part 1
left_list.sort()
right_list.sort()

distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

print(distance)

# Part 2

right_counter = Counter(right_list)
similarity_score = sum(
    left_number * right_counter[left_number] for left_number in left_list)

print(similarity_score)
