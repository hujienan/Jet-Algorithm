from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

solution = Solution()
nums = [-1,0,3,5,9,12]
target = 9
assert solution.search(nums, target) == 4, "Should be 4"