def findMin(nums: List[int]) -> int:
    i, j = 0, len(nums) - 1
    if nums[0] == nums[len(nums) - 1]:
        return nums[0]

    while i < j:
        mid = (i + j) // 2
        left_val = nums[i]
        right_val = nums[j]
        mid_val = nums[mid]
        if mid_val > right_val:
            i = mid + 1
        elif mid_val < right_val:
            j = mid

    return nums[i]
