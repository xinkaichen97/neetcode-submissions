class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            
            if (i, j) in memo:
                return memo[(i, j)]

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                res = dfs(i, j + 2)
                if match:
                    res = res or dfs(i + 1, j)
                memo[(i, j)] = res
                return res

            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = False
            return memo[(i, j)]
        
        return dfs(0, 0)
