class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for i, c in enumerate(s):
            mp[c] = i
        
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, mp[c])
            if i == end:
                res.append(size)
                size = 0
        return res
