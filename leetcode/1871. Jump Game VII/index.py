from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        q = deque([0])
        far = 0
        length = len(s)
        while q:
            i = q.popleft()
            l = max(far + 1, i + minJump)
            r = i + maxJump
            if l <= length - 1 and r >= length - 1:
                return True
            start = l
            while start < r + 1 and start <= length - 1:
                if s[start] == '0':
                    q.append(start)
                start += 1
            far = r
        return False

solution = Solution()
s = "011010"
minJump = 2
maxJump = 3
assert solution.canReach(s, minJump, maxJump) == True, "Should be True"

