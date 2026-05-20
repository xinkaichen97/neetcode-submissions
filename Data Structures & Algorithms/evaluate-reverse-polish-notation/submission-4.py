class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    res = first + second
                elif token == "-":
                    res = first - second
                elif token == "*":
                    res = first * second
                else:
                    res = int(first / second)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]