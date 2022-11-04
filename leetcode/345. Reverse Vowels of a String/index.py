class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = ["a", "e", "i", "o", "u"]
        while left < right:
            l = s[left]
            r = s[right]
            if l.lower() not in vowels:
                left += 1
                continue
            if r.lower() not in vowels:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
            
solution = Solution()
s = "hello"
assert solution.reverseVowels(s) == "holle", "Should be holle"