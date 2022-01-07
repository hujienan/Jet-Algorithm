from typing import DefaultDict, List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = DefaultDict(int)
        trustees = DefaultDict(int)

        for item in trust:
            trusts[item[0]] += 1
            trustees[item[1]] += 1

        for i in range(1, n+1):
            if trusts[i] == 0 and trustees[i] == n-1:
                return i
        return -1

    def findJudge1(self, n: int, trust: List[List[int]]) -> int:
        degree = [0] * (n + 1)
        for x, y in trust:
            degree[x] -= 1
            degree[y] += 1
        for i in range(1, n+1):
            if degree[i] == n-1:
                return i
        return -1


solution = Solution()
assert solution.findJudge(2, [[1, 2]]) == 2, "Should be 2"
assert solution.findJudge1(3, [[1, 3], [2, 3], [3, 1]]) == -1, "Should be -1"
