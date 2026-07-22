def maxProduct(nums: List[int]) -> int:
    length = len(nums)

    ans = min(nums)

    dp_max = 1
    dp_min = 1

    for i in range(length):
        num = nums[i]
        if num == 0:
            dp_max_ = 0
            dp_min_ = 0
        elif num > 0:
            dp_max_ = max(dp_max * num, num)
            dp_min_ = min(dp_min * num, num)
        elif num < 0:
            dp_max_ = max(dp_min * num, num)
            dp_min_ = min(dp_max * num, num)
        dp_max, dp_min = dp_max_, dp_min_
        ans = max(ans, dp_max)

    return ans
