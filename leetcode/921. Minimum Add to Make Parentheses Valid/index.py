class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, r = 0, 0
        for c in s:
            if c == "(":
                l += 1
            elif l == 0:
                r += 1
            else:
                l -= 1
        return l + r


solution = Solution()
s = "())"
assert solution.minAddToMakeValid(s) == 1, "Test case 1 failed"
s = "((("
assert solution.minAddToMakeValid(s) == 3, "Test case 2 failed"
s = "()"
assert solution.minAddToMakeValid(s) == 0, "Test case 3 failed"
s = "()))(("
assert solution.minAddToMakeValid(s) == 4, "Test case 4 failed"
print("All test cases passed")
