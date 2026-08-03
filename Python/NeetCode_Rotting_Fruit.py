from collections import deque

def orangeRotting(grid: List[List[int]]) -> int:
    directions = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    num_rows, num_cols = len(grid), len(grid[0])

    def in_grid(r, c):
        return 0 <= r and r < num_rows and 0 <= c and c < num_cols

    visited = [ [False] * num_cols for _ in range(num_rows) ]
    total = 0

    queue = deque([])
    for i in range(num_rows):
        for j in range(num_cols):
            cell = grid[i][j]
            if cell == 0:
                visited[i][j] = True
            if cell == 2:
                visited[i][j] = True
                queue.append( (i, j) )
                total += 1
            if cell == 1:
                total += 1

    time = -1
    rotted = 0
    while queue:
        time += 1
        new_queue = deque([])
        while queue:
            (i, j) = queue.popleft()
            rotted += 1
            for (dr, dc) in directions:
                if in_grid(i + dr, j + dc) and not visited[i + dr][j + dc]:
                    visited[i + dr][j + dc] = True
                    new_queue.append( (i + dr, j + dc) )
        queue = new_queue

    if rotted == total:
        return max(time, 0)
    return -1
