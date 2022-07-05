def sort(nums):
    length = len(nums)
    for i in range(length):
        min = i
        for j in range(i+1, length):
            if nums[min] > nums[j]:
                min = j
        if min != i:
            nums[min], nums[i] = nums[i], nums[min]
    return nums

nums = [3,2,1,4]
assert sort(nums) == [1,2,3,4], "Should be [1,2,3,4]"