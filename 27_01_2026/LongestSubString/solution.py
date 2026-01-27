class Solution:
    @staticmethod
    def length_of_longest_substring(s):
        max_length = 0
        for x in range(len(s)):
            length = 1
            for y in range(x + 1, len(s)):
                if s[y] in s[x:y]:
                    break
                length += 1
            max_length = max([max_length, length])
        return max_length
