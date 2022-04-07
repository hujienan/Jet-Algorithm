from collections import defaultdict
from operator import eq
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
      dic = defaultdict(list)
      for e in equations:
        if e[1] == '=':
          dic[e[0]].append(e[3])
          dic[e[3]].append(e[0])
      
      def check(c):
        visited.add(c)
        for n in dic[c]:
          if n not in visited:
            check(n)

      for e in equations:
        if e[1] == '!':
          visited = set()
          check(e[0])
          if e[3] in visited:
            return False
      
      return True

solution = Solution()

equations = ['a==b', 'b!=c', 'a==c']
assert solution.equationsPossible(equations) == False, "Should be false"