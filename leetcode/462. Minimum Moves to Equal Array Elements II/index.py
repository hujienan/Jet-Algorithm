from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums) // 2]
        return sum([abs(_ - median) for _ in nums ])

solution = Solution()
nums = [1,2,3]
assert solution.minMoves2(nums) == 2, "Should be 2"