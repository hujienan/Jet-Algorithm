class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] *= num
                else:
                    stack[-1] = int(stack[-1] / num)
                sign = c
                num = 0
        return sum(stack)


solution = Solution()
assert solution.calculate("3+2*2") == 7
assert solution.calculate(" 3/2 ") == 1
assert solution.calculate(" 3+5 / 2 ") == 5
