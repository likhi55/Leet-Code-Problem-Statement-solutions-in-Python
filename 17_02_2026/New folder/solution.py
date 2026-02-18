class Solution:
    @staticmethod
    def read_binary_watch(turnedOn: int):
        def validate_and_convert(bit_fields):
            hour = int(bit_fields[:4], 2)
            mins = int(bit_fields[4:], 2)
            if hour > 11 or mins > 59:
                return "", False
            if mins < 10:
                return f"{hour}:0{mins}", True
            return f"{hour}:{mins}", True

        from itertools import permutations
        if turnedOn > 8:
            return []
        time_list = []
        zeros = 10 - turnedOn
        bits = "1" * turnedOn
        bits += "0" * zeros
        all_combs = {"".join(p) for p in permutations(bits)}
        for comb in all_combs:
            time_item, valid = validate_and_convert(comb)
            if time_item not in time_list and valid:
                time_list.append(time_item)
        return time_list
