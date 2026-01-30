class Solution:
    @staticmethod
    def remove_duplicates(nums):
        n = len(nums)
        nums = list(set(nums))
        m = len(nums)
        nums.extend(["_"] * (n - m))
        return m
