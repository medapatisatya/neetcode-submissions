class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rst = []
        for op in tokens:
            if op == '+':
                y = rst.pop()
                x = rst.pop()
                rst.append(x + y)
            elif op == '-':
                y = rst.pop()
                x = rst.pop()
                rst.append(x - y)
            elif op == '*':
                y = rst.pop()
                x = rst.pop()
                rst.append(x * y)
            elif op == '/':
                y = rst.pop()
                x = rst.pop()
                rst.append(int(x / y))
            else:
                rst.append(int(op))
        return rst[-1]