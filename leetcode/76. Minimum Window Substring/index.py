from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        counter_t = Counter(t)
        # how many unique chars
        required = len(counter_t)
        counter_window = {}
        res = math.inf, 0, 0
        l, r = 0, 0
        formed = 0
        while r < len(s):
            char = s[r]
            if char in counter_t:
                counter_window[char] = counter_window.get(char, 0) + 1
                if counter_window[char] == counter_t[char]:
                    formed += 1
            while formed == required and l <= r:
                if (r-l+1) < res[0]:
                    res = ((r-l+1, l, r))
                removed_char = s[l]
                if removed_char in counter_t:
                    counter_window[removed_char] -= 1
                    if counter_window[removed_char] < counter_t[removed_char]:
                        formed -= 1
                l += 1
            r += 1
        return "" if res[0] == math.inf else s[res[1]:res[2]+1]

solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
assert solution.minWindow(s, t) == 'BANC', """The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t."""