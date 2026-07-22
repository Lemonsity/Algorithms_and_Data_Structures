def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    exists = set()
    counts = dict()
    for card in hand:
        exists.add(card)
        counts[card] = 1 + counts.get(card, 0)

    cards_sorted = sorted(list(exists))

    for card in cards_sorted:
        count = counts[card]
        for i in range(groupSize):
            count_ = counts.get(card + i, 0)
            if count_ < count:
                return False
            counts[card + i] = counts.get(card + i, 0) - count

    return True
