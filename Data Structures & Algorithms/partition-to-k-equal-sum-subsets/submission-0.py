class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # base case
        if sum(nums) % k != 0:
            return False

        # sort descending for early pruning
        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                # backtrack
                used[j] = False
                
                # pruning
                if subsetSum == 0: 
                    return False

            return False

        return backtrack(0, k, 0)
