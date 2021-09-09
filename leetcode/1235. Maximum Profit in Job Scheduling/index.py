from functools import lru_cache
from typing import List
from bisect import bisect_left

class Solution:
    # bottom-up
    def jobScheduling1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        length = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        startTimes = [jobs[_][0] for _ in range(length)]
        @lru_cache(None)
        def dp(index):
            if index == length:
                return 0
            temp = bisect_left(startTimes, jobs[index][1])
            return max(dp(index+1), jobs[index][2] + dp(temp))
        return dp(0)
    # Top-down
    def jobScheduling2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        length = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        startTimes = [jobs[_][0] for _ in range(length)]
        dp = [0] * (length+1)
        for k in range(length-1, -1, -1):
            temp = bisect_left(startTimes, jobs[k][1])
            dp[k] = max(jobs[k][2] + dp[temp], dp[k+1])
        return dp[0]

solution = Solution()
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
assert solution.jobScheduling1(startTime, endTime, profit) == 120, "Should be 120"
assert solution.jobScheduling2(startTime, endTime, profit) == 120, "Should be 120"