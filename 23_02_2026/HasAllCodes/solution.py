class Solution:
    @staticmethod
    def has_all_codes(s: str, k: int) -> bool:
        def generate_all_bits(num):
            combs = []
            for i in range(2 ** num):
                combs.append(format(i, f"0{num}b"))
            return combs

        min_len = (2 ** k) + (k - 1)
        if len(s) < min_len:
            return False
        all_combs = generate_all_bits(k)
        for j in range(len(all_combs) - 1, -1, -1):
            if all_combs[j] not in s:
                return False
        return True
