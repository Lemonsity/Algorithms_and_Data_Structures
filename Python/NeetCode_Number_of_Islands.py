def numIslands(grid: List[List[str]]) -> int:
    num_row = len(grid)
    num_col = len(grid[0])

    visited = [ [False] * num_col for _ in range(num_row) ]

    directions = [(-1,0), (1,0), (0,-1), (0, 1)]

    def in_map(i: int, j: int):
        return 0 <= i and i < num_row and 0 <= j and j < num_col

    def flood(i: int, j: int):
        if not in_map(i, j) or grid[i][j] == "0" or visited[i][j]:
            return

        visited[i][j] = True
        for (dx, dy) in directions:
            flood(i + dx, j + dy)


    total = 0
    for i in range(num_row):
        for j in range(num_col):
            if grid[i][j] == "1" and not visited[i][j]:
                flood(i,j)
                total += 1

    return total
