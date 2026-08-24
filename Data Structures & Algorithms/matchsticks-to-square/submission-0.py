class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # base case
        if sum(matchsticks) % 4 != 0:
            return False

        length = sum(matchsticks) // 4
        sides = [0] * 4
        # sort in descending order to speed up
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    # backtracking
                    sides[j] -= matchsticks[i]
                
                # skip other sides if the current side is empty
                if sides[j] == 0:
                    break
            
            return False
        
        return backtrack(0)
