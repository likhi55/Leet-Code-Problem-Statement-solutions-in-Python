class Solution:
    @staticmethod
    def construct_transformed_array(nums):
        t_arr = [0] * len(nums)
        for i in range(len(nums)):
            idx = (i + nums[i]) % len(nums)
            t_arr[i] = nums[idx]
        return t_arr
