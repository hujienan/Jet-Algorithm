from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def check(heights):
            stack = []
            heights = heights + [0]
            for i, h in enumerate(heights):
                index = i
                while stack and stack[-1][1] > h:
                    p_i, p_h = stack.pop()
                    self.res = max(self.res, p_h * (i - p_i))
                    index = p_i
                stack.append((index, h))
        heights = [ 0 for _ in range(len(matrix[0]))]
        self.res = 0
        for row in matrix:
            heights = [(1 + heights[i]) if v == '1' else 0 for i, v in enumerate(row)]
            check(heights)
        return self.res
        
solution = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
assert solution.maximalRectangle(matrix) == 6, "Should be 6"