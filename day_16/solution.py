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


def find_optimal_paths(grid, rows, cols, end_row, end_col, directions, best_score, distances_from_start):
    queue = []
    seen = set()
    for direction in range(4):
        heapq.heappush(queue, (0, end_row, end_col, direction))
    distances_to_end = {}
    while queue:
        score, row, col, direction = heapq.heappop(queue)
        if (row, col, direction) not in distances_to_end:
            distances_to_end[(row, col, direction)] = score
        if (row, col, direction) in seen:
            continue
        seen.add((row, col, direction))
        dr, dc = directions[(direction + 2) % 4]
        new_row, new_col = row + dr, col + dc
        if 0 <= new_col < cols and 0 <= new_row < rows and grid[new_row][new_col] != '#':
            heapq.heappush(queue, (score + 1, new_row, new_col, direction))
        heapq.heappush(queue, (score + 1000, row, col, (direction + 1) % 4))
        heapq.heappush(queue, (score + 1000, row, col, (direction + 3) % 4))
    optimal_tiles = set()
    for row in range(rows):
        for col in range(cols):
            for direction in range(4):
                if (row, col, direction) in distances_from_start and (row, col, direction) in distances_to_end and distances_from_start[(row, col, direction)] + distances_to_end[(row, col, direction)] == best_score:
                    optimal_tiles.add((row, col))
    return optimal_tiles


with open('16/data.txt') as f:
    data = f.read().strip()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid, rows, cols = init_grid(data)

# * Part 1

# ! IDEA:
# ! The problem is approached using Dijkstra's algorithm to find the shortest path from the start to the end.
# ! The grid is parsed to identify the start ('S') and end ('E') positions.
# ! Dijkstra's algorithm is used to calculate the shortest distance from the start to all other points in the grid.
# ! The algorithm considers moving in four possible directions (up, right, down, left) and also allows for changing direction with a higher cost.
# ! After finding the shortest path to the end, the algorithm is run again in reverse to find the shortest paths from the end to all other points.
# ! The optimal tiles are those that lie on any shortest path from the start to the end.

start_row, start_col, end_row, end_col = find_start_end(grid, rows, cols)
distances_from_start, best_score = dijkstra(
    grid, rows, cols, start_row, start_col, end_row, end_col, directions)

res = best_score
print(res)

# * Part 2

# ! IDEA:
# ! To find the optimal tiles, we need to identify all the tiles that lie on any shortest path from the start to the end.
# ! This is done by running Dijkstra's algorithm again, but this time from the end to all other points in the grid.
# ! By combining the distances from the start to each point and from the end to each point, we can determine which tiles are part of the shortest path.
# ! The optimal tiles are those where the sum of the distances from the start and to the end equals the best score found in the first part.

optimal_tiles = find_optimal_paths(
    grid, rows, cols, end_row, end_col, directions, best_score, distances_from_start)
print(len(optimal_tiles))
