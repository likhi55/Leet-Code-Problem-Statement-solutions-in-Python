class Solution:
    @staticmethod
    def has_alternating_bits(n: int):
        num = bin(n)
        if "11" in num or "00" in num:
            return False
        return True
