from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        cur_res = 1
        max_res = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    cur_res += 1
                else:
                    max_res = max(max_res, cur_res)
                    cur_res = 1
        return max(max_res, cur_res)

solution = Solution()
nums = [100,4,200,1,3,2]
assert solution.longestConsecutive(nums) == 4, "Should be 4"