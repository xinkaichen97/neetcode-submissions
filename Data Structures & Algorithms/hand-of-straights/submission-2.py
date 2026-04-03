class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        counts = defaultdict(int)
        for num in hand:
            counts[num] += 1
            
        for num in hand:
            start = num
            while counts[start - 1]:
                start -= 1
            while start <= num:
                while counts[start]:
                    for i in range(start, start + groupSize):
                        if counts[i] > 0:
                            counts[i] -= 1
                        else:
                            return False
                start += 1

        return True