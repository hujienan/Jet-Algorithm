import math
from collections import deque


class Solution:
    def updateMatrixSolution1(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    top = mat[i-1][j] if i > 0 else math.inf
                    left = mat[i][j-1] if j > 0 else math.inf
                    mat[i][j] = min(top, left) + 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i+1][j] if i < m-1 else math.inf
                    right = mat[i][j+1] if j < n-1 else math.inf
                    mat[i][j] = min(mat[i][j], bottom+1, right+1)
        return mat

    def updateMatrixSolution2(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while q:
            r, c = q.popleft()
            for (x, y) in dirs:
                nr, nc = r + x, c + y
                if nr < 0 or nr >= m or nc < 0 or nc >= n or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat


solution = Solution()
mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert solution.updateMatrixSolution1(mat) == [[0, 0, 0], [0, 1, 0], [
    0, 0, 0]], "Should be [[0,0,0],[0,1,0],[0,0,0]]"
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
assert solution.updateMatrixSolution2(mat) == [[0, 0, 0], [0, 1, 0], [
    1, 2, 1]], "Should be [[0,0,0],[0,1,0],[1,2,1]]"
