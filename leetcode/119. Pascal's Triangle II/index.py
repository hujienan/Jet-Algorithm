from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        cur = [1,1]
        i = 1
        while i < rowIndex:
            newRow = [1]
            for index in range(1, len(cur)):
                newRow.append(cur[index] + cur[index-1])
            newRow.append(1)
            cur = newRow
            i += 1
        return cur

solution = Solution()
rowIndex = 3
assert solution.getRow(rowIndex) == [1,3,3,1], "Should be [1,3,3,1]"