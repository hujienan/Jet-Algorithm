class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] == k - 1:
                stack.pop()
            else:
                if stack and stack[-1][0] == c:
                    stack[-1][1] += 1
                else:
                    stack.append([c, 1])
        res = ""
        for c, n in stack:
            res += c * n
        return res

solution = Solution()
s = "deeedbbcccbdaa"
k = 3
assert solution.removeDuplicates(s, k) == "aa", "Should be aa"