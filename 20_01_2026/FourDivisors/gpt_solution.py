import math


class SolutionGPT:
    @staticmethod
    def sum_four_divisors(nums):
        def sieve(limit_var):
            if limit_var < 2:
                return [False] * (limit_var + 1), []
            is_prime_var = [False, False] + [True] * (limit_var - 1)
            primes_var = []
            for i in range(2, limit_var + 1):
                if is_prime_var[i]:
                    primes_var.append(i)
                    step = i
                    start = i * i
                    if start <= limit_var:
                        for j in range(start, limit_var + 1, step):
                            is_prime_var[j] = False
            return is_prime_var, primes_var

        if not nums:
            return 0
        max_n = max(nums)
        is_prime, primes = sieve(max_n)
        total = 0
        for n in nums:
            if n < 6:  # smallest value with 4 divisors is 6 (2*3)
                continue
            # check p^3
            p = int(round(n ** (1 / 3)))
            # adjust integer cube root safely
            while (p + 1) ** 3 <= n:
                p += 1
            while p ** 3 > n:
                p -= 1
            if p > 1 and p ** 3 == n and is_prime[p]:
                # divisors: 1, p, p^2, p^3
                total += 1 + p + p * p + n
                continue
            # check p * q (two distinct primes)
            limit = int(math.isqrt(n))
            found = False
            for prime in primes:
                if prime > limit:
                    break
                if n % prime == 0:
                    q = n // prime
                    if q != prime and q <= max_n and is_prime[q]:
                        total += 1 + prime + q + n
                    # whether valid or not, we can stop after finding first divisor
                    found = True
                    break
            # no need to do anything if not found or not valid
        return total
