class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
    
    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binary_search(nums, m + 1, r, target)
        else:
            return self.binary_search(nums, l, m - 1, target)