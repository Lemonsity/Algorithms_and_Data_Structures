import heapq

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for i in range(k):
        x, y = points[i][0], points[i][1]
        heapq.heappush_max(heap, (x * x + y * y, points[i]))
    for i in range(k, len(points)):
        furthest = heap[0]
        (furthest_distance, furthest_point) = furthest
        x, y = points[i][0], points[i][1]
        distance = x * x + y * y

        if distance < furthest_distance:
            heapq.heapreplace_max(heap, (distance, point[i]))

    return list(map(lambda x : x[1], heap))
