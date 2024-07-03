from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = float("inf")
        for i in range(4):
            res = min(res, nums[-4 + i] - nums[i])
        return res


solution = Solution()
nums = [5, 3, 2, 4]
assert solution.minDifference(nums) == 0, "Test case 1 failed"
nums = [1, 5, 0, 10, 14]
assert solution.minDifference(nums) == 1, "Test case 2 failed"
