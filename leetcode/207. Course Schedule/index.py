from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {_ : [] for _ in range(numCourses)}
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        visited = set()
        def dfs(n):
            if n in visited:
                return False
            if len(preMap[n]) == 0:
                return True
            visited.add(n)
            for pre in preMap[n]:
                if not dfs(pre):
                    return False
            visited.remove(n)
            preMap[n] = []
            return True
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
        
solution = Solution()
numCourses = 2
prerequisites = [[1,0]]
assert solution.canFinish(numCourses, prerequisites) == True, "Should be True"