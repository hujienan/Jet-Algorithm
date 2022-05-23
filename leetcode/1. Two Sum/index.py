from re import S
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[target - nums[i]] = i

solution = Solution()
nums = [2,7,11,15]
target = 9
assert solution.twoSum(nums, target) == [0,1], "Should be [0,1]"