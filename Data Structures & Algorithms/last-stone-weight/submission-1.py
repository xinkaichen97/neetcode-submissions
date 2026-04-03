class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            smash = stones[-2:]
            stones = stones[:-2]
            print(stones, smash)
            if smash[0] != smash[1]:
                stones.append(smash[1] - smash[0])
        return 0 if len(stones) == 0 else stones[0]