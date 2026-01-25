from solution import Solution

solution = Solution()

inputs = ["()", "()[]{}", "(]", "([])", "([)]"]

for arg in inputs:
    print(solution.is_valid(arg))
