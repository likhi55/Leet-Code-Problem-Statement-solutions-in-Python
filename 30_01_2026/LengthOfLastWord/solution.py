class Solution:
    @staticmethod
    def length_of_last_word(s):
        return len([word for word in s.split(" ") if word != ""][-1])
