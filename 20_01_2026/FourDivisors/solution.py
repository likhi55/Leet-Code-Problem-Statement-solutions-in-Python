class Solution:
    @staticmethod
    def sum_four_divisors(nums):
        def get_divisors(num_var):
            count = 2
            max_div = num_var // 2
            divs = [1, num_var]
            for x in range(2, max_div + 1):
                if num_var % x == 0 and x not in divs:
                    divs.append(x)
                    if x != num_var // x:
                        divs.append(num_var // x)
                        count += 1
                    count += 1
                    if count > 4:
                        return False, 0
            if count < 4:
                return False, 0
            return True, sum(divs)

        sum_ = 0
        completed_nums = {}
        for num in nums:
            if num in list(completed_nums.keys()):
                sum_ += completed_nums[num]
                continue
            four_div, div_s = get_divisors(num)
            completed_nums[num] = div_s
            if four_div:
                sum_ += div_s
        return sum_
