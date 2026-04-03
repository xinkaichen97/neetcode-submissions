class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(op, cls):
            if op == cls == n:
                res.append("".join(subset))
                return 
            if op < n:
                subset.append("(")
                backtrack(op + 1, cls)
                subset.pop()
            if cls < op:
                subset.append(")")
                backtrack(op, cls + 1)
                subset.pop()
        
        backtrack(0, 0)
        return res


