from collections import deque
from math import inf
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp =[-inf] * length
        q = deque()
        dp[0] = nums[0]
        start = 1
        while start < length:
            while q and dp[q[-1]] < dp[start - 1]:
                q.pop()
            q.append(start - 1)
            if start - q[0] > k:
                q.popleft()
            dp[start] = nums[start] + dp[q[0]]
            start += 1
        return dp[length - 1]

solution = Solution()
nums = [1,-1,-2,4,-7,3]
k = 2
assert solution.maxResult(nums, k) == 7, "Should be 7"
