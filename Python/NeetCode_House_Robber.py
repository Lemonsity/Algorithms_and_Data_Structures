def rob(self, nums: List[int]) -> int:
    length = len(nums)
    dp = [0] * (length + 1)
    dp[0] = 0
    dp[1] = nums[0]

    for i in range(2, length + 1):
        dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

    return dp[length]
