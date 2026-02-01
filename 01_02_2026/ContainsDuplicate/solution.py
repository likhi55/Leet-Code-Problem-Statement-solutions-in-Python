class Solution:
    @staticmethod
    def contains_duplicate(nums):
        new_nums = list(set(nums))
        return len(new_nums) != len(nums)
