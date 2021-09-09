from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        x = sum(shifts) % 26
        for i in range(len(s)):
            offset = ord(s[i]) - ord('a')
            ans.append(chr(ord('a') + (offset + x) % 26))
            x = (x - shifts[i]) % 26
        return ''.join(ans)

solution = Solution()
s = "abc"
shifts = [3,5,9]
assert solution.shiftingLetters(s, shifts) == 'rpl', "Should be 'rpl'"