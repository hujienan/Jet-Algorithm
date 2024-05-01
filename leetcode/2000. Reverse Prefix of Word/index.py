class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i != -1:
            return word[: i + 1][::-1] + word[i + 1 :]
        return word


solution = Solution()
word = "abcdef"
ch = "d"
assert solution.reversePrefix(word, ch) == "dcbaef", "Test case 1 failed"
