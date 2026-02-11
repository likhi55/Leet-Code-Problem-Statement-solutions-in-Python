def isBadVersion(num):
    if num >= 1702766719:
        return True
    return False


class Solution:
    @staticmethod
    def first_bad_version(n):
        found = False
        left = 1
        right = n
        avg = 0
        while not found:
            avg = (left + right) // 2
            if isBadVersion(avg):
                if not isBadVersion(avg - 1):
                    return avg
                right = avg
            else:
                left = avg
                if avg == (left + right) // 2:
                    break
        for i in range(avg, n + 1):
            if isBadVersion(i):
                if not isBadVersion(i - 1):
                    return i
        return None
