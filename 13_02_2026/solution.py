class Solution:
    @staticmethod
    def merge_sorted_array(num1, m, num2, n):
        new_num = num1[:m]
        new_num1 = num2[:n]
        new_num.extend(new_num1)
        new_num.sort()
        return new_num
