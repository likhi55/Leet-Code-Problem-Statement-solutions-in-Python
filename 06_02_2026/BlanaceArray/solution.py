class Solution:
    @staticmethod
    def min_removal(nums, k):
        if len(nums) == 0:
            return 0
        nums.sort()
        removed = 0
        i = 0
        for j in range(len(nums)):
            while nums[j] > nums[i] * k:
                i += 1
            removed = max(removed, j - i + 1)
        return len(nums) - removed
