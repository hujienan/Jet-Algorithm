from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        left = right = 0
        res = []
        while right < len(nums):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
            if left > q[0]:
                q.popleft()
            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1
        return res

solution = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
assert solution.maxSlidingWindow(nums, k) == [3,3,5,5,6,7], "Should be [3,3,5,5,6,7]"