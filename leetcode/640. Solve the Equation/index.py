class Solution:
    def solveEquation(self, equation: str) -> str:
        equation = equation.replace('-', '+-')
        parts = equation.split('=')
        
        def process(part):
            xs = 0
            value = 0
            units = part.split('+')
            for unit in units:
                if unit == '':
                    continue
                else:
                    if 'x' in unit:
                        if len(unit) == 1:
                            xs += 1
                        elif len(unit) == 2 and unit[0] == '-':
                            xs -= 1
                        else:
                            xs += int(unit[:-1])
                    else:
                        value += int(unit)
            return xs, value
        
        leftXs, leftValue = process(parts[0])
        rightXs, rightValue = process(parts[1])
        Xs = leftXs - rightXs
        value = rightValue - leftValue
        if Xs == 0:
            if value == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        elif Xs == 1:
            return "x=" + str(value)
        else:
            return "x=" + str(value // Xs)
        
solution = Solution()
equation = "x+5-3+x=6+x-2"
assert solution.solveEquation(equation) == 'x=2', "Output should be x=2"