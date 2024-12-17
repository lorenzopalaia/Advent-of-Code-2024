#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#define MAX_LINES 1000
#define MAX_NUMBERS_PER_LINE 100

int input_list[MAX_LINES][MAX_NUMBERS_PER_LINE];
int line_lengths[MAX_LINES];
int num_lines = 0;

void read_input(const char *filename) {
  FILE *file = fopen(filename, "r");
  if (!file) {
    perror("Failed to open file");
    exit(EXIT_FAILURE);
  }

  char line[256];
  while (fgets(line, sizeof(line), file)) {
    char *token = strtok(line, " ");
    int index = 0;
    while (token) {
      input_list[num_lines][index++] = atoi(token);
      token = strtok(NULL, " ");
    }
    line_lengths[num_lines++] = index;
  }

  fclose(file);
}

bool is_increasing(int *report, int length) {
  for (int i = 0; i < length - 1; i++) {
    if (report[i] >= report[i + 1]) {
      return false;
    }
  }
  return true;
}

bool is_decreasing(int *report, int length) {
  for (int i = 0; i < length - 1; i++) {
    if (report[i] <= report[i + 1]) {
      return false;
    }
  }
  return true;
}

bool is_between_1_and_3(int *report, int length) {
  for (int i = 0; i < length - 1; i++) {
    int diff = abs(report[i + 1] - report[i]);
    if (diff < 1 || diff > 3) {
      return false;
    }
  }
  return true;
}

bool is_safe(int *report, int length) {
  return (is_increasing(report, length) || is_decreasing(report, length)) && is_between_1_and_3(report, length);
}

bool is_monotonic_and_in_range(int *levels, int length) {
  int diffs[MAX_NUMBERS_PER_LINE];
  for (int i = 0; i < length - 1; i++) {
    diffs[i] = levels[i] - levels[i + 1];
  }

  bool is_monotonic = true;
  for (int i = 0; i < length - 1; i++) {
    if (diffs[i] <= 0) {
      is_monotonic = false;
      break;
    }
  }
  if (!is_monotonic) {
    is_monotonic = true;
    for (int i = 0; i < length - 1; i++) {
      if (diffs[i] >= 0) {
        is_monotonic = false;
        break;
      }
    }
  }

  bool is_in_range = true;
  for (int i = 0; i < length - 1; i++) {
    if (abs(diffs[i]) < 1 || abs(diffs[i]) > 3) {
      is_in_range = false;
      break;
    }
  }

  return is_monotonic && is_in_range;
}

int main() {
  read_input("2/data.txt");

  int safe = 0;
  for (int i = 0; i < num_lines; i++) {
    if (is_safe(input_list[i], line_lengths[i])) {
      safe++;
    }
  }
  printf("%d\n", safe);

  safe = 0;
  for (int i = 0; i < num_lines; i++) {
    if (is_monotonic_and_in_range(input_list[i], line_lengths[i])) {
      safe++;
    } else {
      for (int j = 0; j < line_lengths[i]; j++) {
        int tolerated_levels[MAX_NUMBERS_PER_LINE];
        int k = 0;
        for (int l = 0; l < line_lengths[i]; l++) {
          if (l != j) {
            tolerated_levels[k++] = input_list[i][l];
          }
        }
        if (is_monotonic_and_in_range(tolerated_levels, k)) {
          safe++;
          break;
        }
      }
    }
  }
  printf("%d\n", safe);

  return 0;
}