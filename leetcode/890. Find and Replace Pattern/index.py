from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            dic = {}
            match = True
            used = set()
            for i in range(len(word)):
                if pattern[i] in dic:
                    if word[i] != dic[pattern[i]]:
                        match = False
                        break
                else:
                    if word[i] in used:
                        match = False
                        break
                    dic[pattern[i]] = word[i]
                    used.add(word[i])
            if match:
                res.append(word)
        return res

solution = Solution()
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
assert solution.findAndReplacePattern(words, pattern) == ["mee","aqq"], """Should be ["mee","aqq"] """