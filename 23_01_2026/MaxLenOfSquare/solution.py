class Solution:
    @staticmethod
    def max_side_length(mat, threshold):
        max_len = 0
        sqr_len = 1
        m = len(mat)
        n = len(mat[0])
        while sqr_len <= m and sqr_len <= n:
            for i in range(m - sqr_len + 1):
                for j in range(n - sqr_len + 1):
                    sum_val = 0
                    for x in range(sqr_len):
                        sum_val += sum(mat[i + x][j:sqr_len + j])
                    if sum_val <= threshold and max_len < sqr_len:
                        max_len = sqr_len
            sqr_len += 1
        return max_len
