from math import inf
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p: p[0])
        res = 0
        cur_high = -inf
        for low, high in points:
            if low > cur_high:
                res += 1
                cur_high = high
            else:
                cur_high = min(cur_high, high)
        return res

solution = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
assert solution.findMinArrowShots(points) == 2, "Should be 2"