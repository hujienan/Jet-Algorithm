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
            
solution = Solution()
assert solution.findJudge(2, [[1,2]]) == 2, "Should be 2"
assert solution.findJudge(3, [[1,3],[2,3],[3,1]]) == -1, "Should be -1"