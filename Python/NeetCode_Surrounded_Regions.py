def solve(board: List[List[str]]) -> None:
    num_row = len(board)
    num_col = len(board[0])

    marked = [ [False] * num_col for _ in range(num_row)]

    edges = [ (0, j) for j in range(num_col) ] + \
        [ (num_row-1, j) for j in range(num_col) ] + \
        [ (i, 0) for i in range(num_row) ] + \
        [ (i, num_col-1) for i in range(num_row) ]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    def on_map(i, j):
        return 0 <= i and i <  num_row and 0 <= j and j <  num_col

    def flood(i, j):
        if not on_map(i, j) or board[i][j] == "X" or marked[i][j]:
            return

        marked[i][j] = True
        for (dx, dy) in directions:
            flood(i + dx, j + dy)

    for (x, y) in edges:
        flood(x, y)

    for i in range(num_row):
        for j in range(num_col):
            if not marked[i][j]:
                board[i][j] = "X"

    return
