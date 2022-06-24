from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { _ : [] for _ in range(numCourses)}
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        path = set()
        # path to remember all the node on the path we have visited
        res = []
        def dfs(n):
            if n in res:
                # node has already been added, we don't need to search again
                return True
            if n in path:
                # circle found
                return False
            path.add(n)
            for pre in preMap[n]:
                if not dfs(pre):
                    return False
            # start a new path
            path.remove(n)
            # means there is no prerequisite for the current node, we have reached the bottom, so we can safely take this course first
            res.append(n)
            return True
        for n in range(numCourses):
            if not dfs(n):
                # circle found, return empty list
                return []
        return res

solution = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
res = solution.findOrder(numCourses, prerequisites)
assert res == [0,1,2,3], "Should be [0,1,2,3]"