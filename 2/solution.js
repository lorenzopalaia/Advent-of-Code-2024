import { readFileSync } from "fs";

const input_list = readFileSync("2/data.txt", "utf8")
  .trim()
  .split("\n")
  .map((line) => line.split(/\s+/).map(Number));

// * Part 1

const is_increasing = (report) => {
  for (let i = 0; i < report.length - 1; i++) {
    if (report[i] < report[i + 1]) continue;
    else return false;
  }
  return true;
};

const is_decreasing = (report) => {
  for (let i = 0; i < report.length - 1; i++) {
    if (report[i] > report[i + 1]) continue;
    else return false;
  }
  return true;
};

const is_between_1_and_3 = (report) => {
  for (let i = 0; i < report.length - 1; i++) {
    if (
      Math.abs(report[i + 1] - report[i]) >= 1 &&
      Math.abs(report[i + 1] - report[i]) <= 3
    )
      continue;
    else return false;
  }
  return true;
};

const is_safe = (report) => {
  if (
    (is_increasing(report) || is_decreasing(report)) &&
    is_between_1_and_3(report)
  )
    return true;
  else return false;
};

let safe = 0;

for (let i = 0; i < input_list.length; i++) {
  if (is_safe(input_list[i])) safe++;
}

console.log(safe);

// * Part 2

const is_monotonic_and_in_range = (levels) => {
  let diffs = [];
  for (let i = 0; i < levels.length - 1; i++) {
    diffs.push(levels[i] - levels[i + 1]);
  }

  let is_monotonic = true;
  for (let i = 0; i < diffs.length; i++) {
    if (diffs[i] <= 0) {
      is_monotonic = false;
      break;
    }
  }
  if (!is_monotonic) {
    is_monotonic = true;
    for (let i = 0; i < diffs.length; i++) {
      if (diffs[i] >= 0) {
        is_monotonic = false;
        break;
      }
    }
  }

  let is_in_range = true;
  for (let i = 0; i < diffs.length; i++) {
    if (Math.abs(diffs[i]) < 1 || Math.abs(diffs[i]) > 3) {
      is_in_range = false;
      break;
    }
  }

  if (is_monotonic && is_in_range) return true;
  return false;
};

safe = 0;

for (let report of input_list) {
  if (is_monotonic_and_in_range(report)) {
    safe++;
  } else {
    for (let i = 0; i < report.length; i++) {
      let tolerated_levels = report.slice(0, i).concat(report.slice(i + 1));
      if (is_monotonic_and_in_range(tolerated_levels)) {
        safe++;
        break;
      }
    }
  }
}

console.log(safe);
