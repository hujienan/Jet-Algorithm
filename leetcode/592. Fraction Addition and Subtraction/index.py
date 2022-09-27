import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace('-', '+-')
        units = expression.split('+')
        nums = []
        subs = set()
        for unit in units:
            if unit == '':
                continue
            items = unit.split('/')
            nums.append([int(items[0]), int(items[1])])
            subs.add(int(items[1]))
        lcm = math.lcm(*subs)
        value = 0
        for t, d in nums:
            value += t * (lcm // d)
        gcd = math.gcd(value, lcm)
        if gcd == 0:
            return "0/1"
        elif gcd == 1:
            return str(int(value)) + '/' + str(int(lcm))
        else:
            value /= gcd
            lcm /= gcd
            return str(int(value)) + '/' + str(int(lcm))

solution = Solution()
expression = "-1/2+1/2"
assert solution.fractionAddition(expression) == "0/1", "Should be 0/1"