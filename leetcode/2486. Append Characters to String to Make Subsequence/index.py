class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        index = 0
        t_index = 0
        while index < len(s) and t_index < len(t):
            if s[index] == t[t_index]:
                t_index += 1
            index += 1
        return len(t) - t_index


solution = Solution()

s = "coaching"
t = "coding"
assert solution.appendCharacters(s, t) == 4, "Test case 1 failed"

s = "abcde"
t = "a"
assert solution.appendCharacters(s, t) == 0, "Test case 2 failed"

s = "abcde"
t = "f"
assert solution.appendCharacters(s, t) == 1, "Test case 3 failed"

print("PASSED")
