class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])

solution = Solution()
s = "Let's take LeetCode contest"
assert solution.reverseWords(s) == "s'teL ekat edoCteeL tsetnoc", '''Should be "s'teL ekat edoCteeL tsetnoc" '''