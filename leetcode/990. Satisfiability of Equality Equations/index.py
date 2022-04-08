from collections import defaultdict
from typing import List


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



solution = Solution()
equations = ['a==b', 'b!=c', 'a==c']

assert solution.equationsPossible1(equations) == False, "Should be false"
