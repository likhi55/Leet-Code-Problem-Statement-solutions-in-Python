class Solution:
    @staticmethod
    def add_digits(num):
        num_str = str(num)
        sum_val = float('inf')
        while sum_val > 10:
            sum_val = 0
            for c in num_str:
                sum_val += int(c)
            num_str = str(sum_val)
        return sum_val
