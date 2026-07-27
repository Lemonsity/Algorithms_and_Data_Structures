def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    position_speed_pairs = list(zip(position, speed))
    position_speed_pairs.sort()
    position_speed_pairs.reverse()

    stack = []
    stack.append((target - position_speed_pairs[0][0]) / position_speed_pairs[0][1])

    for i in range(1, len(position_speed_pairs)):
        pos = position_speed_pairs[i][0]
        spe = position_speed_pairs[i][1]
        tim = (target - pos) / spe
        if tim > stack[-1]:
            stack.append(tim)

    return len(stack)
