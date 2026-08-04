def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    length = len(gas)
    ans = -1
    for start in range(length):
        remain = 0
        failed = False
        for j in range(length):
            curr = (start + j) % length
            remain += gas[curr]
            if remain >= cost[curr]:
                remain -= cost[curr]
            else:
                failed = True
                break
        if not failed:
            ans = start
            break
    return ans
