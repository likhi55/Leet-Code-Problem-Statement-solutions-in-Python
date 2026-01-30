class Solution:
    @staticmethod
    def climb_stairs(n):
        ser = [1, 1]
        while n + 1 != len(ser):
            ser.append(ser[-1] + ser[-2])
        return ser[n]
