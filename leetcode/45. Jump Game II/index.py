from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, farthest, end = 0, 0, 0
        length = len(nums)
        for i in range(length-1):
            farthest = max(farthest, i + nums[i])
            if end == i:
                steps += 1
                if farthest >= length - 1:
                    return steps
                end = farthest
        return steps

solution = Solution()
nums = [2,3,1,1,4]
assert solution.jump(nums) == 2, "Should be 2"