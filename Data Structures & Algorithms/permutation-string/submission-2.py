class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1, count2 = [0] * 26, [0] * 26
        n = len(s1)
        for i in range(n):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1  
        for i in range(n, len(s2)):
            if count1 == count2:
                return True
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - n]) - ord('a')] -= 1
        return count1 == count2