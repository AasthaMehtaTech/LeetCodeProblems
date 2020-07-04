#mine- math.trunc(a/b)
#eval operation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '*', '-', '/'}
        stack = []
        while len(tokens)>0:
            p = tokens.pop(0)
            if p not in operators:
                stack.append(p)
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(eval(str(n2) + p + str(n1))))

        return int(stack[0])

#diff- lightest
class Solution:
    
    def __init__(self):
        self.operandMap = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": self.div,
        }
    
    @staticmethod
    def div(a, b):
        r = abs(a) // abs(b)
        return r if (a < 0 and b < 0) or (a > 0 and b > 0) else -r

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok.isdigit() or (tok.startswith('-') and tok[1:].isdigit()):
                stack.append(int(tok))
                continue
            op = self.operandMap[tok]
            v2, v1 = stack.pop(), stack.pop()
            result = op(v1, v2)
            stack.append(result)
        return stack.pop()


#fastest
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        if not tokens:
            return 0
        stack = collections.deque()
        operations = ["+","-","*","/"]
        for val in tokens:
            if val in operations:
                first = stack.pop()
                second = stack.pop()
                if val == "+":
                    stack.append(second + first)
                elif val == "-":
                    stack.append(second - first)
                elif val == "*":
                    stack.append(second * first)
                elif val == "/":
                    print(second / first)
                    stack.append(int(second / first))
            else:
                stack.append(int(val))
        return stack[-1]
