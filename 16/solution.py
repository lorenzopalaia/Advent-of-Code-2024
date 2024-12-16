import heapq


def init_grid(data):
    grid = data.split('\n')
    rows = len(grid)
    cols = len(grid[0])
    grid = [[grid[r][c] for c in range(cols)] for r in range(rows)]
    return grid, rows, cols


def find_start_end(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
            if grid[r][c] == 'E':
                end_row, end_col = r, c
    return start_row, start_col, end_row, end_col


def dijkstra(grid, rows, cols, start_row, start_col, end_row, end_col, directions):
    queue = []
    seen = set()
    heapq.heappush(queue, (0, start_row, start_col, 1))
    distances = {}
    best_score = None
    while queue:
        score, row, col, direction = heapq.heappop(queue)
        if (row, col, direction) not in distances:
            distances[(row, col, direction)] = score
        if row == end_row and col == end_col and best_score is None:
            best_score = score
        if (row, col, direction) in seen:
            continue
        seen.add((row, col, direction))
        dr, dc = directions[direction]
        new_row, new_col = row + dr, col + dc
        if 0 <= new_col < cols and 0 <= new_row < rows and grid[new_row][new_col] != '#':
            heapq.heappush(queue, (score + 1, new_row, new_col, direction))
        heapq.heappush(queue, (score + 1000, row, col, (direction + 1) % 4))
        heapq.heappush(queue, (score + 1000, row, col, (direction + 3) % 4))
    return distances, best_score


with open('16/data.txt') as f:
    data = f.read().strip()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid, rows, cols = init_grid(data)

# * Part 1
start_row, start_col, end_row, end_col = find_start_end(grid, rows, cols)
distances_from_start, best_score = dijkstra(
    grid, rows, cols, start_row, start_col, end_row, end_col, directions)

res = best_score
print(res)
