class Solution:
    @staticmethod
    def longest_common_prefix(strs):
        for i in range(len(strs[0])):
            ss = strs[0][0:i + 1]
            present = True
            for s in strs:
                if not s.startswith(ss):
                    present = False
                    break
            if not present:
                return strs[0][0:i]
            elif i + 1 == len(strs[0]) and present:
                return ss
        return ""
