class Solution:
    @staticmethod
    def is_subsequence(s, t):
        idx = []
        for c in s:
            if c not in t:
                return False
            idx.append(t.index(c))
        from copy import deepcopy
        temp = deepcopy(idx)
        temp.sort()
        if idx == temp:
            return True
        return False
