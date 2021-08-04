class Solution:
    def subsets1(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]
        num = nums.pop()
        res = self.subsets1(nums)
        for i in range(len(res)):
            item = res[i][:]
            item.append(num)
            res.append(item)                
        return res
    def subsets2(self, nums: list[int]) -> list[list[int]]:
        def backtrack(first=0, comb=[]):
            if len(comb) == len(nums):
                return
            for i in range(first, len(nums)):
                comb.append(nums[i])
                res.append(comb[:])
                backtrack(i+1, comb)
                comb.pop()
        res = [[]]
        backtrack()
        return res
    
solution = Solution()
assert solution.subsets1([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], "Should be [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]"

assert solution.subsets2([1,2,3]) == [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]], "Should be [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]"

            