class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            have = gas[i] - cost[i]
            if have < 0:
                continue
            curr = (i + 1) % len(gas)
            while curr != i:
                have += gas[curr]
                have -= cost[curr]
                if have < 0:
                    break
                curr = (curr + 1) % len(gas)
                
            if curr == i:
                return i
                
        return -1
