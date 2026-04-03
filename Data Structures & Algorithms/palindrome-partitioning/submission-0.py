class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(subset.copy())
            for j in range(i, len(s)):
                if isPalindrome(s[i : j + 1]):
                    subset.append(s[i : j + 1])
                    backtrack(j + 1)
                    subset.pop()
        
        backtrack(0)
        return res
