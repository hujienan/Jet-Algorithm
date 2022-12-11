from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = [heights[-1]]
        for i in range(len(heights) - 2, -1, -1):
            while len(stack) > 0 and stack[-1] < heights[i]:
                stack.pop()
                res[i] += 1 # each popped out element is the one has been seen by current position
            if stack: # in case the current value is not the highest value (it will see the next greater value)
                res[i] += 1
            stack.append(heights[i])
        return res

solution = Solution()
heights = [10,6,8,5,11,9]
assert solution.canSeePersonsCount(heights) == [3,1,2,1,1,0], "Should be [3,1,2,1,1,0]"