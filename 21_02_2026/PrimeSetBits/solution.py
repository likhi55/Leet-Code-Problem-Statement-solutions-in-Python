class Solution:
    @staticmethod
    def count_prime_set_bits(left: int, right: int) -> int:
        def isprime(num):
            if num < 2:
                return False
            if num in (2, 3):
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            # Check only numbers of the form 6k ± 1
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        prime_set = []
        for n in range(left, right + 1):
            bits = bin(n).count("1")
            if bits in prime_set:
                prime_set.append(bits)
            elif isprime(bits):
                prime_set.append(bits)
        return len(prime_set)
