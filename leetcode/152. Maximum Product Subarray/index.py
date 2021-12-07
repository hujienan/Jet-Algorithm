from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
			
            res = max(res, curMax)
            
        return res
        
solution = Solution()
nums = [2,3,-2,4]
assert solution.maxProduct(nums) == 6, "Should be 6"
