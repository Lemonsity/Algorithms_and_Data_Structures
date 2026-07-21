def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        val = nums[mid]
        if (val == target):
            return mid
        elif (val < target):
            low = mid + 1
        else: # val > target
            high = mid - 1
    return -1
