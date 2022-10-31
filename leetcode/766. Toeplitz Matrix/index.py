from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        j = m + n - 1
        i = 0
        while i < j:
            if i < m:
                r = m - i - 1
                c = 0
            else:
                r = 0
                c = i - m + 1
            val = matrix[r][c]
            r += 1
            c += 1
            while r < m and c < n:
                if matrix[r][c] != val:
                    return False
                r += 1
                c += 1
            i += 1
        return True

solution = Solution()
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
assert solution.isToeplitzMatrix(matrix) == True, " Should be True"