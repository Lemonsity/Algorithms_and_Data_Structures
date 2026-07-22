def canPartition(nums: List[int]) -> bool:
    length = len(nums)

    total = sum(nums)
    if total % 2 == 1:
        return False
    half = total // 2

    prev_dp = [True] + [False] * half
    for i in range(length):
        dp = [False] * (half + 1)
        for j in range(half + 1):
            dp[j] = prev_dp[j] || prev_dp[j - nums[i]]
        prev_dp = dp

    return prev_dp[half]
