from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        ways = [0] * n
        ways[0] = 1
        times = [inf] * n
        times[0] = 0
        pq = [(0, 0)]
        while pq:
            time, node = heappop(pq)
            for nextNode, nextTime in graph[node]:
                totalTime = time + nextTime
                if totalTime < times[nextNode]:
                    times[nextNode] = totalTime
                    ways[nextNode] = ways[node]
                    heappush(pq, (totalTime, nextNode))
                elif totalTime == times[nextNode]:
                    ways[nextNode] += ways[node]
        return ways[-1]

solution = Solution()
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
assert solution.countPaths(n, roads) == 4, "Should be 4"