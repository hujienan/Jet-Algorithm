from typing import TextIO


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                nr, nc = r + x, c + y
                if nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] != 1:
                    continue
                ans += dfs(nr, nc, index)
            return ans
        index = 2
        area = {}
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1
        
        ans = max(area.values() or [0])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                        nx, ny = i + x, j + y
                        if  0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                            seen.add(grid[nx][ny])
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans

solution = Solution()
res = solution.largestIsland([[1,0],[0,1]])
assert res == 3, "Should be 3"
"""
1 0
0 1

to

1 1
0 1
"""
