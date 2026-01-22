class SolutionBest:
    @staticmethod
    def min_bitwise_array(nums):
        res = []
        for a in nums:
            if a % 2 == 0:
                res.append(-1)
            else:
                res.append(a - ((a + 1) & (-a - 1)) // 2)
        return res
