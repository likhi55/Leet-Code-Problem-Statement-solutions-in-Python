class Solution:
    @staticmethod
    def title_to_number(columnTitle):
        num = 0
        columnTitle = columnTitle[::-1]
        for i in range(len(columnTitle)):
            temp = (ord(columnTitle[i]) - 64) * (26 ** i)
            num += temp
        return num
