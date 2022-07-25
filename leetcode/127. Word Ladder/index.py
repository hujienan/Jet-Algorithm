from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + "*" + word[i+1:]
                dic[p].append(word)
        q1 = set([beginWord])
        q2 = set([endWord])
        visited = set([beginWord, endWord])
        res = 1
        while q1 and q2:
            temp = set([])
            for cur in q1:
                for i in range(len(cur)):
                    p = cur[:i] + "*" + cur[i+1:]
                    for word in dic[p]:
                        if word in q2:
                            return res + 1
                        if word not in visited:
                            visited.add(word)
                            temp.add(word)
            q1, q2 = q2, temp
            res += 1
        return 0

solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
assert solution.ladderLength(beginWord, endWord, wordList) == 5, "Should be 5"