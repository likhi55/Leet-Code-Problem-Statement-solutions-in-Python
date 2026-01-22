class Solution:
    @staticmethod
    def minimum_pair_removal(nums):
        ops = 0
        while True:
            import copy
            new_nums = copy.deepcopy(nums)
            new_nums.sort()
            if nums == new_nums:
                break
            min_sum = None
            index = None
            for y in range(len(nums) - 1):
                new_sum = nums[y] + nums[y + 1]
                if min_sum is None or min_sum > new_sum:
                    min_sum = nums[y] + nums[y + 1]
                    index = y
            if index is not None:
                del nums[index]
                del nums[index]
                nums.insert(index, min_sum)
                ops += 1
        return ops

