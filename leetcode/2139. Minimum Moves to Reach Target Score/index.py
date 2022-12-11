class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while maxDoubles and target > 1:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            res += 1
        return res + (target - 1)

solution = Solution()
target = 19
maxDoubles = 2
assert solution.minMoves(target, maxDoubles) == 7, "Should be 7"