class Solution:
    @staticmethod
    def str_str(haystack, needle):
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
