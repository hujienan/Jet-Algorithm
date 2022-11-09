class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s = list(s)
        length = len(s)
        for i in range(length):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                start = stack.pop()
                s[start+1:i] = s[start+1:i][::-1]
        res = [_ for _ in s if _ not in ['(', ')']]
        return "".join(res)
        
solution = Solution()
s = "(ed(et(oc))el)"
assert solution.reverseParentheses(s) == 'leetcode', "Should be leetcode"