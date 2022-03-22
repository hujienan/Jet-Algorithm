from math import comb
from typing import List


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        count_v, count_h = destination
        path = [0] * (count_v + count_h)
        for i in range(len(path)):
          try_h = comb(count_h - 1 + count_v, count_v)
          if try_h >= k:
            path[i] = 'H'
            count_h -= 1
          else:
            path[i] = 'V'
            k -= try_h
            count_v -= 1
        return "".join(path)

solution = Solution()
assert solution.kthSmallestPath([2, 3], 6) == 'HVVHH', "Should be HVVHH"