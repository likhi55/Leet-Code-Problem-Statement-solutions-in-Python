class Solution:
    @staticmethod
    def missing_number(nums):
        n = len(nums)
        val1 = (n * (n + 1)) // 2
        val2 = sum(nums)
        return val1 - val2
