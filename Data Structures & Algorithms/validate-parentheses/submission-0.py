class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dic = {']': '[', ')': '(', '}': '{'}
        for c in s:
            if c in paren_dic:
                if stack and stack[-1] == paren_dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False