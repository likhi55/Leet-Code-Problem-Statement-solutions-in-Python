class BestSolution:
    @staticmethod
    def has_all_codes(s: str, k: int) -> bool:
        needed = 1 << k  # same as 2 ** k
        seen = set()

        # Sliding window: extract substrings of length k
        for i in range(len(s) - k + 1):
            substring = s[i:i + k]
            seen.add(substring)
            if len(seen) == needed:  # early exit
                return True

        return len(seen) == needed
