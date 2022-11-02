from collections import defaultdict
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
        if p != q:
            self.parent[q] = p
    
    def connected(self, p, q):
        p = self.find(p)
        q = self.find(q)
        return p == q
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dic = defaultdict(list)
        for e in equations:
            if e[1] == '=':
                dic[e[0]].append(e[3])
                dic[e[3]].append(e[0])

        def check(start):
            visited.add(start)
            for c in dic[start]:
                if c not in visited:
                    check(c)

        for e in equations:
            if e[1] == '!':
                visited = set()
                check(e[0])
                if e[3] in visited:
                    return False

        return True

    def equationsPossible1(self, equations: List[str]) -> bool:
        dic = defaultdict(list)
        for e in equations:
            if e[1] == '=':
                dic[e[0]].append(e[3])
                dic[e[3]].append(e[0])

        colors = defaultdict(list)
        for k in dic:
            stack = [k]
            while stack:
                c = stack.pop()
                for n in dic[c]:
                    if n not in colors[k]:
                        colors[k].append(n)
                        stack.append(n)

        for e in equations:
            if e[1] == '!':
                if e[0] == e[3]:
                    return False
                if e[3] in colors[e[0]]:
                    return False
        return True

    def equationsPossible2(self, equations: List[str]) -> bool:
        # union find way
        uf = UF(26)
        base = ord('a')
        for e in equations:
            if e[1] == '=':
                uf.union(ord(e[0]) - base, ord(e[3]) - base)
   
        for e in equations:
            if e[1] == '!':
                if uf.connected(ord(e[0]) - base, ord(e[3]) - base):
                    return False
        return True

solution = Solution()
equations = ['a==b', 'b!=c', 'a==c']

assert solution.equationsPossible2(equations) == False, "Should be false"
