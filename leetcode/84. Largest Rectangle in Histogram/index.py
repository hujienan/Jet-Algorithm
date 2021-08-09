class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [0]
        res = 0
        newHeights = [0]
        for i in range(len(heights)):
            newHeights.append(heights[i])
        newHeights.append(0)
        for i in range(len(newHeights)):
            while newHeights[stack[-1]] > newHeights[i]:
                top = stack.pop()
                res = max(res, newHeights[top] * (i - stack[-1] - 1))
            stack.append(i)
        return res


solution = Solution()
assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "Should be 10"
