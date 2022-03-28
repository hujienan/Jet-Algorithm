from functools import lru_cache
from math import inf
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1):
            return -1
        @lru_cache(None)
        def dp(i, j, piles):
            if i == j and piles == 1:
                return 0
            if piles == 1:
                return sum(stones[i:j+1]) + dp(i, j, k)
            res = inf
            for mid in range(i, j, k-1):
                cur = dp(i, mid, 1) + dp(mid+1, j, piles-1)
                res = min(res, cur)
            return res
        return dp(0, n-1, 1)

solution = Solution()
stones = [3,5,1,2,6]
k = 3
assert solution.mergeStones(stones, k) == 25, "Should be 25"