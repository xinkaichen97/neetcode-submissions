class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([ch.lower() for ch in s if ch.isalnum()])
        start, end = 0, len(s) - 1
        while start < len(s):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
