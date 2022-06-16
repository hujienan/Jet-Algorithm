from typing import List


class Solution:
    def isBipartite1(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        seen = {}
        for i in range(length):
            if i not in seen:
                stack = [i]
                seen[i] = True
                while stack:
                    cur = stack.pop()
                    for nei in graph[cur]:
                        if nei not in seen:
                            seen[nei] = not seen[cur]
                            stack.append(nei)
                        elif seen[nei] == seen[cur]:
                            return False
        return True

    def isBipartite2(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        seen = {}
        def dfs(node):
            for nei in graph[node]:
                if nei not in seen:
                    seen[nei] = not seen[node]
                    if dfs(nei):
                        return False
                elif seen[nei] == seen[node]:
                    return False
            return True
        for i in range(length):
            if i not in seen:
                seen[i] = True
                if not dfs(i):
                    return False
        return True


solution = Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
assert solution.isBipartite1(graph) == False, "Should be false"
assert solution.isBipartite2(graph) == False, "Should be false"