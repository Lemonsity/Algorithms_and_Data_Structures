def longestPalindrome(s: str) -> str:
    length = len(s)
    dp = [ [False] * length for _ in range(length) ]

    ans = s[0:1]

    for i in range(length):
        dp[i][i] = True
    for i in range(length - 1):
        dp[i][i+1] = s[i] == s[i+1]

    for sub_length in range(3, length + 1):
        for i in range(0, length + 1 - sub_length):
            j = i + sub_length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True

    for sub_length in range(1, length + 1):
        for i in range(0, length + 1 - sub_length):
            if dp[i][i + sub_length - 1]:
                ans = s[i : i+sub_length]
    return ans
