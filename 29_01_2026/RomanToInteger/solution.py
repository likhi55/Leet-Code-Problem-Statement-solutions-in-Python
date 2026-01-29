class Solution:
    @staticmethod
    def roman_to_int(s):
        sym_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        num = 0
        i = 0
        while i < len(s) - 1:
            if sym_val[s[i]] < sym_val[s[i + 1]]:
                num += sym_val[s[i:i + 2]]
                i += 2
                continue
            num += sym_val[s[i]]
            i += 1

        if i != len(s):
            num += sym_val[s[-1]]

        return num
