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

def canComplete(gas: List[int], cost: List[int]) -> int:
    length = len(gas)
    end, start = 0, length - 1
    tank = gas[start]
    while end < start:
        print(tank, start, end)
        if cost[end - 1] <= tank:
            print("one")
            tank -= cost[end - 1]
            tank += gas[end]
            end += 1
        elif tank < cost[end - 1]:
            print("two")
            start -= 1
            tank += gas[start]
            tank -= cost[start]
    print(tank, start, end)
    if cost[end - 1] <= tank:
        return start
    return -1
