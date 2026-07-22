def jump(nums: List[int]) -> int:
    length = len(nums)
    sub_problems = [1001] * length
    sub_problems[length - 1] = 0
    for i in range(length - 1, -1, -1):
        for j in range(1, nums[i] + 1):
            if (i + j >= length):
                break
            sub_problems[i] = min(sub_problems[i], 1 + sub_problems[i + j])
    return sub_problems[0]
