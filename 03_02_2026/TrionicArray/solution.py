class Solution:
    @staticmethod
    def is_trionic(nums):
        brk1 = None
        brk2 = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1] and brk1 is None:
                brk1 = i
            elif nums[i] < nums[i + 1] and brk1 is not None and brk2 is None:
                brk2 = i
                break
        if brk1 is None or brk2 is None:
            return False
        inc_arr1 = nums[0: brk1 + 1]
        inc_arr2 = nums[brk2:]
        dec_arr = nums[brk1: brk2 + 1]
        if inc_arr1[-1] != dec_arr[0] or dec_arr[-1] != inc_arr2[0] or len(inc_arr1) == 1 or len(inc_arr1) != len(list(
                set(inc_arr1))) or len(inc_arr2) != len(list(set(inc_arr2))) or len(dec_arr) != len(list(set(dec_arr))):
            return False
        dec_arr = dec_arr[::-1]
        import copy

        c1_arr = copy.deepcopy(inc_arr1)
        c2_arr = copy.deepcopy(inc_arr2)
        c3_arr = copy.deepcopy(dec_arr)
        c1_arr.sort()
        c2_arr.sort()
        c3_arr.sort()
        return (inc_arr1 == c1_arr) and (c2_arr == inc_arr2) and (c3_arr == dec_arr)
