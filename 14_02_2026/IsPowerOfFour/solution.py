class Solution:
    @staticmethod
    def is_power_of_four(n):
        nums = []
        if n <= 0:
            return False
        x = 0
        while n >= 4 ** x:
            nums.append(4 ** x)
            x += 1
        if n in nums:
            return True
        return False
