from copy import copy
from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        numberOfWalls = 0
        while [_ for row in isInfected for _ in row if _ == 1]:
            table = copy.deepcopy(isInfected)
            # paint components
            def paint(i, j, c):
                if i < 0 or j < 0 or i >= m or j >= n or table[i][j] == 0 or table[i][j] == c:
                    return
                if table[i][j] == 1:
                    table[i][j] = c
                    paint(i - 1, j, c)
                    paint(i + 1, j, c)
                    paint(i, j - 1, c)
                    paint(i, j + 1, c)
            components = {}
            color = 97
            for i in range(m):
                for j in range(n):
                    if table[i][j] == 1:
                        c = chr(color)
                        color += 1
                        components[c] = (i ,j)
                        paint(i, j, c)
            dic = {}
            res = None
            def findThreatedCells(i, j, d = ''):
                if i < 0 or j < 0 or i >= m or j >= n or (i, j, d) in visited or table[i][j] == '':
                    return
                visited.add((i, j, d))
                if table[i][j] == 0:
                    cells.add((i, j))
                    walls.add((i, j, d))
                    return
                findThreatedCells(i - 1, j, 'up')
                findThreatedCells(i + 1, j, 'down')
                findThreatedCells(i, j - 1, 'left')
                findThreatedCells(i, j + 1, 'right')
            
            for c in components:
                i, j = components[c]
                cells = set()
                visited = set()
                walls = set()
                findThreatedCells(i, j)
                dic[c] = (cells, walls)
                if not res:
                    res = c
                else:
                    if len(dic[res][0]) < len(dic[c][0]):
                        res = c
            numberOfWalls += len(dic[res][1])
            # contain
            for i in range(m):
                for j in range(n):
                    if table[i][j] == res:
                        isInfected[i][j] = ""
            # spread
            for item in dic:
                if item is not res:
                    cells = dic[item][0]
                    for i, j in cells:
                        if isInfected[i][j] == 0:
                            isInfected[i][j] = 1
        return numberOfWalls        
        
solution = Solution()
isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
assert solution.containVirus(isInfected) == 10, "Should be 10"