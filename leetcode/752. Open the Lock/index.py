from collections import deque
from typing import List


class Solution:
    def openLock1(self, deadends: List[str], target: str) -> int:
        # BFS
        q = deque(['0000'])
        visited = set(deadends)
        if '0000' in visited:
            return -1
        steps = 0
        while q:
            for _ in range(len(q)):
                s = q.popleft()
                if s in visited:
                    continue
                visited.add(s)
                if s == target:
                    return steps
                for i in range(4):
                    for d in (-1, 1):
                        new_s = s[:i] + str((int(s[i]) + d) % 10) + s[i+1:]
                        q.append(new_s)
            steps += 1
        return -1
    def openLock2(self, deadends: List[str], target: str) -> int:
        # both ways BFS
        visited = set(deadends)
        if '0000' in visited:
            return -1
        q1 = set(['0000'])
        q2 = set([target])
        steps = 0
        while q1 and q2:
            temp = set()
            for s in q1:
                if s in visited:
                    continue
                visited.add(s)
                if s in q2:
                    return steps
                for i in range(4):
                    for d in (-1, 1):
                        new_s = s[:i] + str((int(s[i]) + d) % 10) + s[i+1:]
                        temp.add(new_s)
            steps += 1
            q1 = q2
            q2 = temp
        return -1
solution = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
assert solution.openLock1(deadends, target) == 6, "Should be 6"
assert solution.openLock2(deadends, target) == 6, "Should be 6"