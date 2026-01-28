class Solution:
    @staticmethod
    def is_palindrome(x):
        s = str(x)
        if s == s[::-1]:
            return True
        return False
