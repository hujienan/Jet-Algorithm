from functools import lru_cache
from math import inf
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = [[s.count('0'), s.count('1')] for s in strs]
        @lru_cache(None)
        def dp(index, i, j):
            if i > m or j > n:
                return -inf
            if index == len(strs):
                return 0
            return max(dp(index + 1, i, j), 1 + dp(index+1, i + counter[index][0], j + counter[index][1]))
        
        return dp(0, 0, 0)
        

solution = Solution()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
assert solution.findMaxForm(strs, m, n) == 4, "Should be 4"