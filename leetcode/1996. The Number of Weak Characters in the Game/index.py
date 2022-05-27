from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        items = sorted(properties, key = lambda x:(x[0], -x[1]))
        stack = []
        for x, y in items:
            while stack and stack[-1] < y:
                stack.pop()
            stack.append(y)
        return len(items) - len(stack)
        
solution = Solution()
properties = [[5,5],[6,3],[3,6]]
assert solution.numberOfWeakCharacters(properties) == 0, "Should be 0"