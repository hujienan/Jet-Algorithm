class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        b_count = 0
        for c in s:
            if c == "a":
                res = min(res + 1, b_count)
            else:
                b_count += 1
        return res


solution = Solution()

s = "aababbab"

assert solution.minimumDeletions(s) == 2, "Test case 1 failed"

s = "bbaaaaabb"

assert solution.minimumDeletions(s) == 2, "Test case 2 failed"

s = "aaaaa"

assert solution.minimumDeletions(s) == 0, "Test case 3 failed"

print("PASSED")
