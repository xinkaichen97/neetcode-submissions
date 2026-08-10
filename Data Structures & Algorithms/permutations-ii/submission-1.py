class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        # hashmap
        count = {num: 0 for num in nums}
        for num in nums:
            count[num] += 1

        def dfs():
            # base case
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            # try every number with count > 0
            for num in count:
                if count[num] > 0:
                    curr.append(num)
                    count[num] -= 1
                    dfs()
                    # backtrack
                    count[num] += 1
                    curr.pop()

        dfs()
        return res
        