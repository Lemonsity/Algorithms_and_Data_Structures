import heapq

def leastInterval(tasks: List[str], n : int) -> int:
    if len(tasks) == 0:
        return 0

    counts = dict()
    for task in tasks:
        counts[task] = 1 + counts.get(task, 0)

    heap = []
    for (task, count) in counts.items():
        heapq.heappush_max(heap, (n, count, task))

    time = 0
    while heap:
        (top_elapsed, top_count, top_task) = heapq.heappop_max(heap)

        to_elapse = max(n - top_elapsed, 0) + 1
        time += to_elapse

        print(top_elapsed, top_count, top_task, time)

        new_heap = []
        while heap:
            (elapsed, count, task) = heapq.heappop_max(heap)
            heapq.heappush_max(new_heap, (min(elapsed + to_elapse, n), count, task))
        if (top_count > 1):
            heapq.heappush_max(new_heap, (0, top_count - 1, top_task))

        heap = new_heap

    return time
