def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    [l, r] = newInterval

    length = len(intervals)
    if length == 0:
        return [newInterval]

    index = -1
    for i in range(length):
        [li, ri] = intervals[i]
        if l <= ri:
            index = i
            break

    if index == -1:
        index = length

    def overlapped(interval1, interval2):
        return (interval1[0] <= interval2[0] and interval2[0] <= interval1[1]) or \
            (interval2[0] <= interval1[0] and interval1[0] <= interval2[1])

    def merge(interval1, interval2):
        assert overlapped(interval1, interval2)
        if interval1[0] <= interval2[0]:
            return [ interval1[0], max(interval1[1], interval2[1]) ]
        else:
            return [ interval2[0], max(interval1[1], interval2[1]) ]

    if index == length or not overlapped(intervals[index], newInterval):
        intervals.insert(index, newInterval)
        return intervals

    intervals[index] = merge(intervals[index], newInterval)
    flag = True
    while flag and index < len(intervals) - 1:
        if not overlapped(intervals[index], intervals[index + 1]):
            flag = False
            continue
        intervals[index] = merge(intervals[index], intervals[index + 1])
        intervals.pop(index + 1)

    return intervals
