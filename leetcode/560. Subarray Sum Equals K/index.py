from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        m = {0: 1}
        for num in nums:
            total += num
            if total - k in m:
                res += m[total - k]
            m[total] = m.get(total, 0) + 1
        return res

solution = Solution()
nums = [1,1,1]
k = 2
assert solution.subarraySum(nums, k) == 2, "Should be 2"