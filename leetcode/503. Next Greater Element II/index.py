from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        stack = []
        res = [-1] * length
        for i in range(2 * length - 1, -1, -1):
            while stack and stack[-1] <= nums[i % length]:
                stack.pop()
            if stack:
                res[i % length] = stack[-1]
            stack.append(nums[i % length])
        return res

solution = Solution()
nums = [1,2,3,4,3]
assert solution.nextGreaterElements(nums) == [2,3,4,-1,4], "Should be [2,3,4,-1,4]"