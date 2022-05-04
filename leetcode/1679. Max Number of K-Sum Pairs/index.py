from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        res = 0
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] == k:
                res += 1
                left += 1
                right -= 1
            else:
                left += 1
        return res

solution = Solution()
nums = [3,1,3,4,3]
k = 6
assert solution.maxOperations(nums, k) == 1, "Should be 1"