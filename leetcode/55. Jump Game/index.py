from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        length = len(nums)
        for i in range(length):
            if maxReach >= i:
                maxReach = max(maxReach, i + nums[i])
            if maxReach >= length - 1:
                return True
        return False
        
solution = Solution()
nums = [2,3,1,1,4]
assert solution.canJump(nums) == True, "Should be True"