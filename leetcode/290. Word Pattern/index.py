class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_p = list(pattern)
        list_s = s.split()
        if len(list_p) != len(list_s):
            return False
        if not len(set(pattern)) == len(set(list_s)):
            return False
        m = {}
        for i in range(len(list_p)):
            if list_p[i] not in m:
                m[list_p[i]] = list_s[i]
            else:
                if m[list_p[i]] != list_s[i]:
                    return False
        return True
  
solution = Solution()
assert solution.wordPattern('abba', 'dog dog dog dog') == False, "Should be False"
assert solution.wordPattern('abba', 'dog cat cat dog') == True, "Should be True"
