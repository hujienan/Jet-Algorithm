class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            for i in range(len(s)):
                if s.count(s[i]) > 1:
                    return True
            return False
        else:
            diffs = [i for i in range(len(s)) if s[i] != goal[i]]
            if len(diffs) != 2:
                return False
            s = list(s)
            s[diffs[0]], s[diffs[1]] = s[diffs[1]], s[diffs[0]]
            return "".join(s) == goal

solution = Solution()
s = "ab"
goal = "ba"
assert solution.buddyStrings(s, goal) == True, "Should be true"