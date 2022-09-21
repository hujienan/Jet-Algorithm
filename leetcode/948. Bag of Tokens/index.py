from collections import deque
from lib2to3.pgen2 import token
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        q = deque(tokens)
        res = 0
        while q:
            if q[0] <= power:
                res += 1
                power -= q.popleft()
            else:
                if len(q) > 1 and res > 0:
                    res -= 1
                    power += q.pop()
                else:
                    break
        return res

solution = Solution()
tokens = [100,200,300,400]
power = 200
assert solution.bagOfTokensScore(tokens, power) == 2, "Should be 2"