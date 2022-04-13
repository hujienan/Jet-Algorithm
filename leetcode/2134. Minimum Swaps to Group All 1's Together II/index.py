from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_size = nums.count(1)
        cur_zeros = nums[:window_size].count(0)
        res = cur_zeros
        left = 1
        new_nums = nums + nums
        length = len(nums)
        while left < length:
            if new_nums[left+window_size-1] == 0:
                cur_zeros += 1
            if new_nums[left - 1] == 0:
                cur_zeros -= 1
            res = min(res, cur_zeros)
            left += 1
        return res

solution = Solution()
nums = [1,1,0,0,1]
assert solution.minSwaps(nums) == 0, "Should be 0"