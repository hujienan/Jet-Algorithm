from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : -x[1])
        res = 0
        for x, y in boxTypes:
            num = min(truckSize, x)
            res += (num * y)
            truckSize -= num
            if not truckSize:
                return res
        return res

solution = Solution()
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
assert solution.maximumUnits(boxTypes, truckSize) == 8, "Should be 8"