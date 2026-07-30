def lengthOfLIS(nums: List[int]) -> int:
    length = len(nums)
    dp = [1] * length

    for i in range(length):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
    return max(dp)
