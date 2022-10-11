from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def t(n, path = []):
            path.append(n)
            if n == len(graph) - 1:
                res.append(path[:])
            for num in graph[n]:
                t(num, path)
            path.remove(n)
        t(0)
        return res

solution = Solution()
graph = [[1,2],[3],[3],[]]
assert solution.allPathsSourceTarget(graph) == [[0,1,3],[0,2,3]], "Should be [[0,1,3],[0,2,3]]"