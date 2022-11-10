from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                dic[num] = stack[-1]
            else:
                dic[num] = -1
            stack.append(num)
        return [dic[_] for _ in nums1]

solution = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
assert solution.nextGreaterElement(nums1, nums2) == [-1,3,-1], "Should be [-1,3,-1]"