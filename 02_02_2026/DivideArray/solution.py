class Solution:
    @staticmethod
    def minimum_cost(nums):
        cost = 0
        import copy
        new_nums = copy.deepcopy(nums)
        indices = []
        while len(indices) != 3:
            min_value = min(new_nums)
            min_index = nums.index(min_value)
            if min_index in indices:
                min_index = nums.index(min_value, min_index + 1)
                indices.append(min_index)
                del new_nums[new_nums.index(min_value)]
                continue
            indices.append(min_index)
            del new_nums[new_nums.index(min_value)]
        if 0 not in indices:
            cost += nums[0]
            cost += nums[indices[0]]
            cost += nums[indices[1]]
            return cost
        cost += nums[indices[2]]
        cost += nums[indices[0]]
        cost += nums[indices[1]]
        return cost
