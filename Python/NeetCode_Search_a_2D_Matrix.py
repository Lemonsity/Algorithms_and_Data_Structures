def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row_len = len(matrix)
    col_len = len(matrix[0])

    found_row = False
    candidate_row = -1
    i, j = 0, row_len - 1
    while i < j:
        mid = (i + j) // 2
        mid_l, mid_r = matrix[mid][0], matrix[mid][col_len - 1]
        if mid_l <= target and target <= mid_r:
            found_row = True
            candidate_row = mid
            break
        elif target < mid_l:
            j = mid - 1
        elif mid_r < target:
            i = mid + 1

    if not found_row:
        candidate_row = i

    print(candidate_row)

    found = False
    i, j = 0, col_len - 1
    while i <= j:
        mid = (i + j) // 2
        mid_val = matrix[candidate_row][mid]
        print(i, j, mid, mid_val)
        if mid_val == target:
            return True
        elif target < mid_val:
            j = mid - 1
        elif target > mid_val:
            i = mid + 1
    return False
