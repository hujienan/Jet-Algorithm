from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(start = 0, comb = []):
            res.append(comb)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                comb.append(nums[i])
                bt(i+1, comb[:])
                comb.pop()
        bt()
        return res

solution = Solution()
nums = [1,2,2]
assert solution.subsetsWithDup(nums) == [[],[1],[1,2],[1,2,2],[2],[2,2]], "Should be [[],[1],[1,2],[1,2,2],[2],[2,2]]"