def merge(nums, low, mid, high):
    temp = nums[:]
    i = low
    j = mid + 1
    for p in range(low, high+1):
        if i == mid + 1:
            # left is done
            nums[p] = temp[j]
            j += 1
        elif j == high + 1:
            # right is done
            nums[p] = temp[i]
            i += 1
        elif temp[i] > temp[j]:
            # use left
            nums[p] = temp[j]
            j += 1
        else:
            # use right
            nums[p] = temp[i]
            i += 1
def sort(nums, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    sort(nums, low, mid)
    sort(nums, mid + 1, high)
    merge(nums, low, mid, high)
def mergeSort(nums):
    sort(nums, 0, len(nums) - 1)
    return nums

nums = [3,2,1,4]
assert mergeSort(nums) == [1,2,3,4], "Should be [1,2,3,4]"