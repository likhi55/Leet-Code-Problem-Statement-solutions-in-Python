class Solution:
    @staticmethod
    def generate(numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        ret = [[1], [1, 1]]
        for x in range(2, numRows):
            arr = [1]
            for y in range(x - 1):
                arr.append(ret[x - 1][y] + ret[x - 1][y + 1])
            arr.append(1)
            ret.append(arr)
        return ret
