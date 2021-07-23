def partition(nums, l, r):
  pivot = nums[r]
  i = l
  for j in range(l, r):
    if nums[j] < pivot:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
  nums[i], nums[r] = nums[r], nums[i]
  return i

def quickSort(nums, l, r):
  if l >= r:
    return
  pivot_index = partition(nums, l, r)
  quickSort(nums, l, pivot_index - 1)
  quickSort(nums, pivot_index+1, r)

a = [10,2,1,3,52,2,4, -1]
quickSort(a, 0, len(a)-1)
assert a == [-1, 1, 2, 2, 3, 4, 10, 52], "Result is wrong"


