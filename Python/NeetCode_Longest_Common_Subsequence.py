def longestCommonSubsequence(text1: str, text2: str) -> int:
    len_1, len_2 = len(text1), len(text2)

    dp = [ [0] * (len_2 + 1) for _ in range(len_1 + 1) ]
    for i in range(0, len_1):
        for j in range(0, len_2):
            dp[i+1][j+1] = max(dp[i][j] + 1 if text1[i] == text2[j] else 0, \
                           dp[i][j+1], \
                           dp[i+1][j])

    return dp[len_1][len_2]
