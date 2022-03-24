from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            # if (l, r) in dic:
            #     return dic[(l, r)]
            # dic[(l, r)] = 0
            res = 0
            for i in range(l, r+1):
                cur = nums[l-1] * nums[i] * nums[r+1]
                cur += dfs(l, i-1) + dfs(i+1, r)
                # dic[(l, r)] = max(cur, dic[(l, r)])
                res = max(cur, res)
            return res
        nums = [1] + nums + [1]
        # dic = {}
        return dfs(1, len(nums)-2)
        
solution = Solution()
assert solution.maxCoins([3,1,5,8]) == 167, "Should be 167"
        
        
    
    
    