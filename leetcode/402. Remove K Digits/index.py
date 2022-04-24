from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = deque()
        for n in num:
            while q and k and q[-1] > n:
                q.pop()
                k -= 1
            if q or n != '0':
                q.append(n)
        while k:
            if q:
                q.pop()
            k -= 1
        return ''.join(q) or '0'

solution = Solution()
num = "1432219"
k = 3
assert solution.removeKdigits(num, k) == '1219', "Should be 1219"
        