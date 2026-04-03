class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand.sort()
        counts = Counter(hand)
        for num in hand:
            if counts[num]:
                for i in range(num, num + groupSize):
                    if not counts[i]:
                        return False
                    counts[i] -= 1
        return True