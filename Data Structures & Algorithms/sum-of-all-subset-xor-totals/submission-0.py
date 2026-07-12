class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0

        def backtrack(curr, i):
            nonlocal res
            xor = 0
            for num in curr:
                xor ^= num
            res += xor

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        backtrack([], 0)
        return res
