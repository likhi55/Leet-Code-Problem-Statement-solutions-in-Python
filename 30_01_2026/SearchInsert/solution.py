class Solution:
    @staticmethod
    def search_insert(nums, target):
        for x in range(len(nums)):
            if target <= nums[x]:
                return x
        return x + 1
