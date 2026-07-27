def minWindow(s: str, t: str) -> str:
    s_len = len(s)

    def c_to_i(c):
        return ord(c) - ord('A')

    def gte(count_1, count_2):
        flag = True
        for i in range(ord('z') - ord('A') + 1):
            flag = flag and count_1[i] >= count_2[i]
        return flag

    count_t = [0] * (ord('z') - ord('A') + 1)
    for c in t:
        count_t[c_to_i(c)] += 1

    l, r = 0, 0
    found = False
    ans, ans_len = s, s_len
    count_curr = [0] * (ord('z') - ord('A') + 1)
    while r <= s_len:
        if gte(count_curr, count_t):
            if r - l <= len(ans):
                found = True
                ans, ans_len = s[l:r], r - l
            count_curr[c_to_i(s[l])] -= 1
            l += 1
        if not gte(count_curr, count_t):
            if r == s_len:
                break
            count_curr[c_to_i(s[r])] += 1
            r += 1

    if not found:
        return ""
    return ans
