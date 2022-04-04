from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = heights + [0]
        res = 0
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                p_i, p_h = stack.pop()
                res = max(res, p_h * (i - p_i))
                index = i
            stack.append((index, h))
        return res


solution = Solution()
assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "Should be 10"
