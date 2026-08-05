def exists(board: List[List[str]], word: str) -> bool:
    num_row, num_col = len(board), len(board[0])

    directions = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    def in_bound(i, j):
        return 0 <= i and i < num_row and 0 <= j and j < num_col

    def aux(suffix: str, i, j, visited):
        if suffix == "":
            return True
        if not in_bound(i, j) or suffix[0] != board[i][j] or (i, j) in visited:
            return False

        ans = False
        visited.add( (i, j) )
        for (di, dj) in directions:
            ans = ans or aux(suffix[1:], i + di, j + dj, visited)
        visited.remove( (i, j) )
        return ans

    ans = False
    for i in range(num_row):
        for j in range(num_col):
            ans = ans or aux(word, i, j, set())

    return ans
