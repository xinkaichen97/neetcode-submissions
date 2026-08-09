class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(curr):
            # base case
            if len(curr) == len(nums):
                res.add(tuple(curr))
                return

            # iterate through nums
            for i in range(len(nums)):

                if nums[i] != float("-inf"):
                    curr.append(nums[i])
                    nums[i] = float("-inf")

                    # backtracking
                    backtrack(curr)
                    nums[i] = curr[-1]
                    curr.pop()

        backtrack([])
        return list(res)
        