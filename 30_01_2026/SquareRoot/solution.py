class Solution:
    @staticmethod
    def my_sqrt(x):
        if x == 0:
            return x
        for i in range(x + 1):
            if i ** 2 == x:
                return i
            elif i ** 2 > x:
                return i - 1
        return 0
