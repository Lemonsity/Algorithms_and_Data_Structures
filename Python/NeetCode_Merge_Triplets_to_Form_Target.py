def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    [at, bt, ct] = target
    candidates = []
    for [ai, bi, ci] in triplets:
        if ai <= at and bi <= bt and ci <= ct:
            candidates.append([ai, bi, ci])

    a, b, c = 0, 0, 0
    for [ai, bi, ci] in candidates:
        a = max(a, ai)
        b = max(b, bi)
        c = max(c, ci)

    return a == at and b == bt and c == ct
