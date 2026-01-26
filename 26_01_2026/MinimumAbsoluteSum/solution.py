class Solution:
    @staticmethod
    def minimum_abs_difference(arr):
        min_diff = None
        diff_pairs = []
        arr.sort()
        for i in range(1, len(arr)):
            if min_diff is None or min_diff > arr[i] - arr[i - 1]:
                min_diff = arr[i] - arr[i - 1]
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                diff_pairs.append([arr[i-1], arr[i]])
        diff_pairs.sort()
        return diff_pairs
