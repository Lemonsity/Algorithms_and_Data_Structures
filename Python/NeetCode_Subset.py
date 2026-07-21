import copy

def subsets(nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return [[]]

    sub_result = subsets(nums[1:])
    new_result = []
    for result in sub_result:
        result_copy = copy.copy(result)
        result_copy.append(nums[0])
        new_result.append(result_copy)

    sub_result.extend(new_result)
    return sub_result
