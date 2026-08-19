class Solution:
    def reorganizeString(self, s: str) -> str:
        # calculate counts
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # get max index and freq
        max_idx = freq.index(max(freq))
        max_freq = freq[max_idx]
        # return empty string if freq too high
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = [''] * len(s)
        idx = 0
        max_char = chr(max_idx + ord('a'))

        # place max_char at 0, 2, 4, ...
        while freq[max_idx] > 0:
            res[idx] = max_char
            idx += 2
            freq[max_idx] -= 1

        # place the remaining chars
        for i in range(26):
            while freq[i] > 0:
                if idx >= len(s):
                    idx = 1
                res[idx] = chr(i + ord('a'))
                idx += 2
                freq[i] -= 1

        return ''.join(res)
