class Solution:
    @staticmethod
    def reverse_bits(n):
        bits = format(n, "b")
        bits = "0" * (32 - len(bits)) + bits
        bits = bits[::-1]
        return int(bits, 2)
