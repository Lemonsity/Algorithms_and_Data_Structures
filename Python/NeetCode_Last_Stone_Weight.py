import heapq

def lastStoneWeight(stones: List[int]) -> int:
    heapq.heapify_max(stones)
    print(stones)
    while len(stones) >= 2:
        s1 = heapq.heappop_max(stones)
        s2 = heapq.heappop_max(stones)
        if (s1 != s2):
            heapq.heappush_max(stones, abs(s1 - s2))
        print(stones)

    if len(stones) == 1:
        return stones[0]
    return 0
