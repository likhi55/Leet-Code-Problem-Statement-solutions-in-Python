class Solution:
    @staticmethod
    def get_lucky(s, k):
        char_sum = ""
        for c in s:
            char_sum += str(ord(c) - 96)
        char_num = int(char_sum)
        for i in range(k):
            sum_val = 0
            for c in str(char_num):
                sum_val += int(c)
            char_num = sum_val
        return char_num
