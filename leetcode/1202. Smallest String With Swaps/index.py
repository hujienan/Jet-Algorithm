from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n):
                self.parent = [_ for _ in range(n)]
            
            def find(self, p):
                if p != self.parent[p]:
                    self.parent[p] = self.find(self.parent[p])
                return self.parent[p]
            
            def union(self, p, q):
                p = self.find(p)
                q = self.find(q)
                if p!= q:
                    self.parent[q] = p

            def connected(self, p, q):
                return self.find(p) == self.find(q)
        uf = UF(len(s))
        for i, j in pairs:
            uf.union(i, j)
        parents = defaultdict(list)
        for i in range(len(s)):
            parents[uf.find(i)].append(s[i])
        for p in parents:
            parents[p].sort(reverse=True)
        res = ""
        for i in range(len(s)):
            res += parents[uf.find(i)].pop()
        return res
        
solution = Solution()
s = "dcab"
pairs = [[0,3],[1,2]]
assert solution.smallestStringWithSwaps(s, pairs) == "bacd","Should be bacd"