class Solution:
    @staticmethod
    def two_sum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]
        return None
