def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if x == 1:
        return 0

    positive, abs_n = n > 0, abs(n)

    dp = [0] * 11
    dp[0] = x
    for i in range(1, 11):
        dp[i] = dp[i - 1] * dp[i - 1]
    print(dp)

    positive_pow = 1
    for i in range(0, 11):
        if ((abs_n >> i) & 1) == 1:
            print(i)
            positive_pow *= dp[i]

    return positive_pow if positive else (1 / positive_pow)
