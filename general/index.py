def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for p in range(left, right):
        if nums[p] < pivot:
            nums[i], nums[p] = nums[p], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i

def sort(nums, left, right):
    if left >= right:
        return
    mid = partition(nums, left, right)
    sort(nums, left, mid-1)
    sort(nums, mid+1, right)

nums = [3,2,1,4]
sort(nums, 0, len(nums)-1)
assert nums == [1,2,3,4], "Should be [1,2,3,4]"