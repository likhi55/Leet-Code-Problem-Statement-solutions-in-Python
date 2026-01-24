class SolutionSecond:
    @staticmethod
    def min_deletion_size(strs):
        n = len(strs[0])
        del_cols = 0
        for x in range(n):
            for i in range(len(strs) - 1):
                if ord(strs[i][x]) > ord(strs[i + 1][x]):
                    del_cols += 1
                    break
        return del_cols
