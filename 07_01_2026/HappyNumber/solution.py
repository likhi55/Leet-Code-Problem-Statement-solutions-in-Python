class Solution:
    @staticmethod
    def is_happy(n):
        sum_val = float("inf")
        str_num = str(n)
        sums = []
        while sum_val != 1:
            sum_val = 0
            for c in str_num:
                sum_val += int(c) ** 2
            str_num = str(sum_val)
            if sum_val in sums:
                return False
            sums.append(sum_val)
        return True
