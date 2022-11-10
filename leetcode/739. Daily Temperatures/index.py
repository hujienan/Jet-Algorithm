from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        stack = []
        for i in range(length-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

solution = Solution()
temperatures = [73,74,75,71,69,72,76,73]
assert solution.dailyTemperatures(temperatures) == [1,1,4,2,1,1,0,0], "Should be [1,1,4,2,1,1,0,0]"