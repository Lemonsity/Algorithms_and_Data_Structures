def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    total = len(intervals)
    swapped = [ (i[1], i[0]) for i in intervals ]
    sorted_by_end_time = sorted(swapped)

    min_start_time = min( [ i[0] for i in intervals ] )
    curr_end_time, count = min_start_time, 0
    for (end, start) in sorted_by_end_time:
        if curr_end_time <= start:
            count += 1
            curr_end_time = end

    return total - count
