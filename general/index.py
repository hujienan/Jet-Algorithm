# def partition(nums, left, right):
#     q = nums[right]
#     i = left
#     for j in range(left, right):
#         if nums[j] < q:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#     nums[i], nums[right] = nums[right], nums[i]
#     return i

# def quickSort(nums, left, right):
#     if left >= right:
#         return
#     p = partition(nums, left, right)
#     quickSort(nums, left, p-1)
#     quickSort(nums, p+1, right)

# nums = [3,2,1,4]
# quickSort(nums, 0, len(nums) - 1)
# assert nums == [1,2,3,4], "Should be [1,2,3,4]"

# def mergeSort(nums, low, high):
#     if low == high:
#         return
#     mid = (low + high) // 2
#     mergeSort(nums, low, mid)
#     mergeSort(nums, mid+1, high)
#     i = low
#     j = mid+1
#     temp = nums[:]
#     for p in range(low, high+1):
#         if i > mid:
#             nums[p] = temp[j]
#             j += 1
#         elif j > high:
#             nums[p] = temp[i]
#             i += 1
#         elif temp[i] > temp[j]:
#             nums[p] = temp[j]
#             j += 1
#         else:
#             nums[p] = temp[i]
#             i += 1
# nums = [3,2,1,4]
# mergeSort(nums, 0, len(nums) - 1)
# assert nums == [1,2,3,4], "Should be [1,2,3,4]"

def partition(nums, left, right):
    p = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] < p:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[right], nums[i] = nums[i], nums[right]
    return i

def sort(nums, left, right):
    if left >= right:
        return
    p = partition(nums, left, right)
    sort(nums, left, p-1)
    sort(nums, p+1, right)
nums = [3,2,1,4]
sort(nums, 0, len(nums)-1)
print(nums)
