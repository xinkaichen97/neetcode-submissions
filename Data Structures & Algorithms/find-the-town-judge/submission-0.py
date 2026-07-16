class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        diff = defaultdict(int)

        for src, dst in trust:
            diff[src] -= 1
            diff[dst] += 1

        for i in range(1, n + 1):
            if diff[i] == n - 1:
                return i

        return -1
