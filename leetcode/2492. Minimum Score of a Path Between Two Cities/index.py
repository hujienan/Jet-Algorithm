from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for road in roads:
            graph[road[0]].append([road[1], road[2]])
            graph[road[1]].append([road[0], road[2]])

        self.res = inf
        visited = set()

        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            for nei, score in graph[cur]:
                self.res = min(self.res, score)
                dfs(nei)
        dfs(1)
        return self.res


solution = Solution()
n = 4
roads = [[1, 2, 2], [1, 3, 4], [3, 4, 7]]
assert solution.minScore(n, roads) == 2
