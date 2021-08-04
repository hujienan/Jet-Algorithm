class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def bt(first=1, comb=[]):
            if len(comb) == k:
                res.append(comb[:])
                return
            for num in range(first, n+1):
                comb.append(num)
                bt(num+1, comb)
                comb.pop()
        res = []
        bt()
        return res


solution = Solution()
assert solution.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [
    3, 4]], "Should be [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]"
