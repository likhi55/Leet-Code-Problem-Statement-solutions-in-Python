class Solution:
    @staticmethod
    def majority_element(nums):
        m = len(nums) // 2
        unique_element = set(nums)
        for element in unique_element:
            if nums.count(element) > m:
                return element
        return 0
