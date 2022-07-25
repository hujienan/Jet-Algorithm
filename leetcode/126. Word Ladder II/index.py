from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + "*" + word[i+1:]
                dic[p].append(word)
        q = deque([(beginWord, 1)])
        length = 0
        visited = set()
        path = defaultdict(set)
        while q:
            cur, k = q.popleft()
            if cur == endWord:
                length = k
                break
            if cur not in visited:
                visited.add(cur)
                for i in range(len(cur)):
                    p = cur[:i] + '*' + cur[i+1:]
                    for word in dic[p]:
                        if word not in visited:
                            path[word].add(cur)
                            q.append((word, k+1))
        res = []
        q = deque([(endWord, [endWord])])
        while q:
            word, cur_path = q.popleft()
            if word == beginWord:
                res.append(cur_path[::-1])
            if len(cur_path) == length:
                continue
            for w in path[word]:
                if w not in cur_path:
                    new_path = cur_path[:]
                    new_path.append(w)
                    q.append((w, new_path))
        return res

solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
assert solution.findLadders(beginWord, endWord, wordList) == [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]], '''Should be [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]'''
