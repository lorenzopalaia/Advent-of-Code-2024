#include <stdio.h>
#include <stdlib.h>

#define MAX_LINES 1000

void read_input(int input_list[MAX_LINES][2], int *line_count) {
  FILE *file = fopen("1/data.txt", "r");
  if (!file) {
    perror("Failed to open file");
    exit(EXIT_FAILURE);
  }

  *line_count = 0;
  while (fscanf(file, "%d %d", &input_list[*line_count][0], &input_list[*line_count][1]) == 2) {
    (*line_count)++;
  }

  fclose(file);
}

int compare(const void *a, const void *b) {
  return (*(int *)a - *(int *)b);
}

int main() {
  int input_list[MAX_LINES][2];
  int left_list[MAX_LINES], right_list[MAX_LINES];
  int line_count;

  read_input(input_list, &line_count);

  for (int i = 0; i < line_count; i++) {
    left_list[i] = input_list[i][0];
    right_list[i] = input_list[i][1];
  }

  // Part 1
  qsort(left_list, line_count, sizeof(int), compare);
  qsort(right_list, line_count, sizeof(int), compare);

  int distance = 0;
  for (int i = 0; i < line_count; i++) {
    distance += abs(left_list[i] - right_list[i]);
  }

  printf("%d\n", distance);

  // Part 2
  int max_value = 0;
  for (int i = 0; i < line_count; i++) {
    if (right_list[i] > max_value) {
      max_value = right_list[i];
    }
  }

  int *right_counter = calloc(max_value + 1, sizeof(int));
  if (!right_counter) {
    perror("Failed to allocate memory");
    exit(EXIT_FAILURE);
  }

  for (int i = 0; i < line_count; i++) {
    right_counter[right_list[i]]++;
  }

  int similarity_score = 0;
  for (int i = 0; i < line_count; i++) {
    if (left_list[i] <= max_value) {
      similarity_score += left_list[i] * right_counter[left_list[i]];
    }
  }

  free(right_counter);

  printf("%d\n", similarity_score);

  return 0;
}