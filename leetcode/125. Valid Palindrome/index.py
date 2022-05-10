class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(filter(str.isalnum, s)).lower()
        return a == a[::-1]

solution = Solution()
s = "A man, a plan, a canal: Panama"
assert solution.isPalindrome(s) == True, "Should be true"