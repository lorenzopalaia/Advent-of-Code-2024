import { readFileSync } from "fs";

const input_list = readFileSync("1/data.txt", "utf8")
  .trim()
  .split("\n")
  .map((line) => line.split(/\s+/).map(Number));

const left_list = [];
const right_list = [];

for (let i = 0; i < input_list.length; i++) {
  left_list.push(input_list[i][0]);
  right_list.push(input_list[i][1]);
}

// Part 1
left_list.sort((a, b) => a - b);
right_list.sort((a, b) => a - b);

const distance = left_list.reduce(
  (sum, l, i) => sum + Math.abs(l - right_list[i]),
  0
);

console.log(distance);

// Part 2
const right_counter = right_list.reduce((counter, num) => {
  counter[num] = (counter[num] || 0) + 1;
  return counter;
}, {});

const similarity_score = left_list.reduce(
  (sum, left_number) => sum + left_number * (right_counter[left_number] || 0),
  0
);

console.log(similarity_score);
