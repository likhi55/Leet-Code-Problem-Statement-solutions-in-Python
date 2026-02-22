class Solution:
    @staticmethod
    def binary_gap(n: int) -> int:
        indexes = [i for i, c in enumerate(bin(n)) if c == "1"]
        if len(indexes) == 1:
            return 0
        diffs = [indexes[j + 1] - indexes[j] for j in range(len(indexes) - 1)]
        return max(diffs)
