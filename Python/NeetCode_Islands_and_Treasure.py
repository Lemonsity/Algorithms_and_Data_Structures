from collections import deque

def islandsAndTreasure(grid: List[List[int]]) -> None:
    ISLAND = 2147483647

    row_len = len(grid)
    col_len = len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def in_bound(i, j):
        return 0 <= i and i < row_len and 0 <= j and j < col_len

    queue = deque([])

    for (i, j) in [(i, j) for i in range(row_len) for j in range(col_len)]:
        if grid[i][j] == 0:
            queue.append((i, j, 0))

    while queue:
        (i, j, dist) = queue.popleft()

        grid[i][j] = min(grid[i][j], dist)
        for (dx, dy) in directions:
            i_, j_ = i + dx, j + dy
            if in_bound(i_, j_) and grid[i_][j_] == ISLAND:
                queue.append((i_, j_, dist + 1))

    return
