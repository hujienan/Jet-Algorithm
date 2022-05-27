import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        items = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        piles = []
        for item in items:
            v = item[1]
            i = bisect.bisect_left(piles, v)
            if i == len(piles):
                piles.append(v)
            else:
                piles[i] = v
        return len(piles)

solution = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
assert solution.maxEnvelopes(envelopes) == 3, "Should be 3"