class Solution:
    @staticmethod
    def min_bitwise_array(nums):
        def check_power_2(num):
            rem = 0
            while rem != 1:
                num = num // 2
                rem = num % 2
            if num == 1:
                return True
            return False

        new_list = []
        for x in nums:
            if x == 2 or x % 2 == 0:
                new_list.append(-1)
            elif check_power_2(x + 1):
                new_list.append(x // 2)
            elif (x - 1) % 4 == 0:
                new_list.append(x - 1)
            else:
                power = 0
                while x > (2 ** power):
                    power += 1
                for i in range(2 ** (power - 1), x):
                    if i | (i + 1) == x:
                        new_list.append(i)
                        break
        return new_list
