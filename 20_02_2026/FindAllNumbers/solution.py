class Solution:
    @staticmethod
    def find_disappeared_numbers(nums):
        all_nums = list(range(1, len(nums) + 1))
        return list(set(all_nums) - set(nums))
