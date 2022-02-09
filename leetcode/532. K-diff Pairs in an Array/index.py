from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numsCount = {}
        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1
        res = 0
        for key in numsCount:
            if k == 0 and numsCount[key] > 1:
                res += 1
            elif k > 0 and key + k in numsCount:
                res += 1
        return res

solution = Solution()
assert solution.findPairs([3,1,4,1,5], 2) == 2, "Should be 2"