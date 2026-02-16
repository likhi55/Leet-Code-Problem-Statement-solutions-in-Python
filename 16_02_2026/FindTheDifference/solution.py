class Solution:
    @staticmethod
    def find_the_difference(s: str, t: str) -> str:
        while True:
            if len(s) != 0:
                c = s[0]
                count1 = s.count(c)
                count2 = t.count(c)
                if count1 == count2:
                    s = s.replace(c, "")
                    t = t.replace(c, "")
                else:
                    return s[0]
            else:
                return t
