class Solution:
    @staticmethod
    def count_binary_substrings(s):
        count = 0
        half_len = len(s) // 2
        for i in range(1, half_len + 1):
            req_ss1 = ("0" * i) + ("1" * i)
            count += s.count(req_ss1)
            count += s.count(req_ss1[::-1])
        return count
