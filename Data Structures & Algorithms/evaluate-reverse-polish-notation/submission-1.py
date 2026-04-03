class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = eval(f"{num1} {token} {num2}")
                stack.append(int(res))
        return stack[0]