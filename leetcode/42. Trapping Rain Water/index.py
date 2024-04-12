from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left = [0] * length
        right = [0] * length
        left[0] = height[0]
        for i in range(1, length):
            left[i] = max(left[i - 1], height[i])
        right[length - 1] = height[length - 1]
        for i in range(length - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        res = 0
        for i in range(length):
            res += min(left[i], right[i]) - height[i]
        return res


solution = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
assert solution.trap(height) == 6, "Should be 6"
