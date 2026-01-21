from new_solution import SolutionNew
from solution import Solution

solution = Solution()
new_solution = SolutionNew()

input_data = [[559, 511], [932, 618], [-623, -443], [431, 91], [838, -127]]
print(solution.min_time_to_visit_all_points(input_data))

input_data = [[559, 511], [932, 618], [-623, -443], [431, 91], [838, -127]]
print(new_solution.min_time_to_visit_all_points(input_data))
