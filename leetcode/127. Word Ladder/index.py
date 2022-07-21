from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dic = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + '*' + word[i+1:]
                dic[p].append(word)
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for i in range(len(w)):
                    p = w[:i] + '*' + w[i+1:]
                    for word in dic[p]:
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
            res += 1
        return 0

solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
assert solution.ladderLength(beginWord, endWord, wordList) == 5, "Should be 5"