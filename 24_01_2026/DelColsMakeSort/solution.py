class Solution:
    @staticmethod
    def min_deletion_size(strs):
        n = len(strs[0])
        del_cols = 0
        for x in range(n):
            arr = [string[x] for string in strs]
            import copy
            copy_arr = copy.deepcopy(arr)
            copy_arr.sort()
            if arr != copy_arr:
                del_cols += 1
        return del_cols
