import math

def minEatingSpeed(piles: List[int], h : int) -> int:
    optimal = int(1e9)
    low = 1
    high = int(1e9)
    while low <= high:
        rate = low + (high - low) // 2
        h_used = 0
        for pile in piles:
            h_used += math.ceil(pile / rate)

        print(low, high, rate, h_used)


        if h_used > h:
            low = rate + 1
        if h_used <= h:
            optimal = min(optimal, rate)
            high = rate - 1

    return optimal
