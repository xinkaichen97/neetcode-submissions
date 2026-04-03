class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}

        def dfs(i):
            if i in memo:
                return memo[i]

            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i : i + len(word)]:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return memo[i]
            
            memo[i] = False
            return memo[i]

        return dfs(0)
