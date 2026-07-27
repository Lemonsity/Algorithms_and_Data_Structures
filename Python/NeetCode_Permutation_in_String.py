def checkInclusion(s1: str, s2: str) -> bool:
    s1_len = len(s1)
    s2_len = len(s2)
    if s2_len < s1_len:
        return False

    target_counts = [0] * 26
    for c in s1:
        target_counts[ord(c) - ord('a')] += 1

    ans, flag = False, True
    counts = [0] * 26
    for i in range(s1_len):
        counts[ord(s2[i]) - ord('a')] += 1
    for c in range(0, 26):
        flag = flag and counts[c] == target_counts[c]
    ans = ans or flag

    for j in range(s1_len, s2_len):
        c1, c2 = ord(s2[j - s1_len]) - ord('a'), ord(s2[j]) - ord('a')
        counts[c1] -= 1
        counts[c2] += 1

        flag = True
        for c in range(0, 26):
            flag = flag and counts[c] == target_counts[c]
        ans = ans or flag

    return ans
