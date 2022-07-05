def sort(nums):
    length = len(nums)
    for i in range(length-1, -1, -1):
        swap = False
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = True
        if not swap:
            break
    return nums

nums = [3,2,1,4]
assert sort(nums) == [1,2,3,4], "Should be [1,2,3,4]"