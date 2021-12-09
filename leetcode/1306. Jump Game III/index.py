from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = set()
        q = deque([start])

        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            vis.add(i)

            l, r = i - arr[i], i + arr[i]

            if not l in vis and l > -1:
                q.append(l)

            if not r in vis and r < n:
                q.append(r)

        return False


solution = Solution()
assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 5) == True, "Should be True"
