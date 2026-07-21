def dailyTemperatures(temperatures: List[int]) -> List[int]:
    length = len(temperatures)
    result = [0] * length

    stack = []
    for i in range(length):
        curr_temperature = temperatures[i]
        while stack:
            (temperature, index) = stack[-1]
            if curr_temperature > temperature:
                result[index] = i - index
                stack.pop()
                continue
            break
        stack.append((curr_temperature, i))

    return result
