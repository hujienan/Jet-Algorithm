class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

solution = Solution()
s = "leEeetcode"
assert solution.makeGood(s) == 'leetcode', "Should be leetcode"