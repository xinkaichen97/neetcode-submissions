class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0] * len(s)
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if memo[i]:
                return memo[i]

            memo[i] = dfs(i + 1)
            if i < len(s) - 1:
                if s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456":
                    memo[i] += dfs(i + 2)

            return memo[i]

        return dfs(0)