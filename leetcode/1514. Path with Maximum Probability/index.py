from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            graph[a].append((b,p))
            graph[b].append((a,p))
        probTo = [0] * n
        probTo[start] = 1
        pq = [(-1, start)]
        while pq:
            p, node = heappop(pq)
            if node == end:
                return -p
            for nextNode, nextP in graph[node]:
                newP = p * nextP
                if newP < probTo[nextNode]:
                    probTo[nextNode] = newP
                    heappush(pq, (newP, nextNode))
        return 0

solution = Solution()
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
assert solution.maxProbability(n, edges, succProb, start, end) == 0.25, "Should be 0.25"