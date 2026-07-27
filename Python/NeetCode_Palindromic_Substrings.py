def countSubstrings(s: str) -> int:
    length = len(s)
    count = 0
    dp = [ [False] * (length + 1) for _ in range(length + 1) ]

    for i in range(length + 1):
        dp[i][i] = True
    for i in range(length):
        dp[i][i+1] = True
        count += 1

    for sub_len in range(2, length + 1):
        for i in range(length - sub_len + 1):
            index_l, index_r = i, i + sub_len
            is_pal = (dp[index_l + 1][index_r - 1] and s[index_l] == s[index_r - 1])
            dp[index_l][index_r] = is_pal
            count += 1 if is_pal else 0

    return count
