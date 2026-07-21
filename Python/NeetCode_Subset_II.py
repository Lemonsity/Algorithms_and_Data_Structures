def subsetWithDup(nums: List[int]) -> List[List[int]]:
    sorted_nums = sorted(nums)

    def sublist_without_head(nums: List[int]):
        length = len(nums)
        if length == 0:
            return []

        head = nums[0]
        index = 0
        while index < length and nums[index] == head:
            index += 1
        return nums[index:]

    def aux(nums: List[int]):
        if len(nums) == 0:
            return [[]]

        head = nums[0]
        sub_1 = aux(nums[1:])
        sub_2 = aux(sublist_without_head(nums))

        return [ [head] + sub for sub in sub_1 ] + sub_2

    return aux(sorted_nums)
