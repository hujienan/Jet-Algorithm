import collections


class DSU:
    def __init__(self) -> None:
        self.par = [_ for _ in range(1001)]

    def find(self, x):
        if self.par[x] != x:
            return self.find(self.par[x])
        return x

    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot:
            return False
        self.par[xroot] = yroot
        return True

class Solution:
    def findRedundantConnection1(self, edges: list[list[int]]) -> list[int]:

        graph = collections.defaultdict(set)

        def hasPath(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(hasPath(nei, target) for nei in graph[source])
            return False

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and hasPath(u, v):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)
    
    def findRedundantConnection2(self, edges: list[list[int]]) -> list[int]:

        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge


solution = Solution()
# DFS
assert solution.findRedundantConnection1([[1,2],[1,3],[2,3]]) == [2,3], "Should be [2, 3]"

# DSU

assert solution.findRedundantConnection2([[1,2],[1,3],[2,3]]) == [2,3], "Should be [2, 3]"

