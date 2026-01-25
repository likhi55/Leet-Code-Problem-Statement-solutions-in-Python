class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        if len(s) == 0:
            return True
        return False
