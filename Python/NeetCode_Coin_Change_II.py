def change(amount: int, coins: List[int]) -> int:
    prev = [0] * (amount + 1)
    prev[0] = 1

    for coin in coins:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for a in range(1, amount + 1):
            dp[a] += prev[a]
            if a >= coin:
                dp[a] += dp[a - coin]
        prev = dp

    return prev[amount]
