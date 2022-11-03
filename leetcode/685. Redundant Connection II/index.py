from typing import List


class UF:
    def __init__(self, size):
        self.parent = [-1] * size
        for i in range(size):
            self.parent[i] = i

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)
        self.parent[q] = p

    def connected(self, p, q):
        p = self.find(p)
        q = self.find(q)
        return p == q


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = set()
        biParent = None
        for u, v in edges:
            if v in parents:
                biParent = v
                break
            parents.add(v)

        def detectCircle(edges, skipEdge=[]):
            uf = UF(len(edges) + 1)
            for u, v in edges:
                if [u, v] == skipEdge:
                    continue
                if uf.connected(u, v):
                    return [u, v]
                uf.union(u, v)
            return False

        if not biParent:
            return detectCircle(edges)

        for u, v in edges[::-1]:
            if v == biParent:
                if not detectCircle(edges, [u, v]):
                    return [u, v]


solution = Solution()
edges = [[1, 2], [1, 3], [2, 3]]
assert solution.findRedundantDirectedConnection(
    edges) == [2, 3], "Should be [2,3]"
