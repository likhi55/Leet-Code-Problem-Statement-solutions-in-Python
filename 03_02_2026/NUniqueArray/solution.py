class Solution:
    @staticmethod
    def sum_zero(n):
        arr = []
        if n == 1:
            return [0]
        if n % 2 == 0:
            for i in range(n // 2):
                arr.append(i + 1)
                arr.append(-i - 1)
        else:
            for i in range(n // 2 - 1):
                arr.append(i + 1)
                arr.append(-i - 1)
            arr.append(-n)
            arr.append(n // 2)
            arr.append(n // 2 + 1)
        return arr
