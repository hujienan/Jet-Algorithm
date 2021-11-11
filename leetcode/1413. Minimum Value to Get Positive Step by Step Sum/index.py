from typing import List


class Solution:
    def minStartValue1(self, nums: List[int]) -> int:
        n = len(nums)
        m = 100
        left = 1
        right = m * n + 1
        while left < right:
            middle = (left + right) // 2
            total = middle
            is_valid = True
            for num in nums:
                total += num
                if total < 1:
                    is_valid = False
                    break
            if is_valid:
                right = middle
            else:
                left = middle + 1
        return left

    def minStartValue2(self, nums: List[int]) -> int:
        min_val = 0
        total = 0
        for num in nums:
            total += num
            min_val = min(min_val, total)
        return -min_val + 1

solution = Solution()
nums = [-3,2,-3,4,2]
assert solution.minStartValue1(nums) == 5, "Should be 5"
assert solution.minStartValue2(nums) == 5, "Should be 5"
