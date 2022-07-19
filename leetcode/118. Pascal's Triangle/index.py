from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        i = 2
        while i < numRows:
            newRow = [1]
            for index in range(1, len(res[-1])):
                newRow.append(res[-1][index] + res[-1][index-1])
            newRow.append(1)
            res.append(newRow)
            i += 1
        return res

solution = Solution()
numRows = 5
assert solution.generate(numRows) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], "Should be [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"