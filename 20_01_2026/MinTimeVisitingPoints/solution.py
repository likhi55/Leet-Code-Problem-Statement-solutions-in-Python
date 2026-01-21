class Solution:
    @staticmethod
    def min_time_to_visit_all_points(points):
        seconds = 0
        for x in range(len(points)):
            if x + 1 == len(points):
                break
            current = points[x]
            next_p = points[x + 1]
            while True:
                px = next_p[0] - current[0]
                py = next_p[1] - current[1]
                pass
                if px > 0 and py > 0:
                    current[0] += 1
                    current[1] += 1
                    seconds += 1
                elif px == 0 and py == 0:
                    break
                elif px == 0:
                    seconds += 1
                    if py > 0:
                        current[1] += 1
                        continue
                    current[1] -= 1
                elif py == 0:
                    seconds += 1
                    if px > 0:
                        current[0] += 1
                        continue
                    current[0] -= 1
                elif px < 0 and py < 0:
                    current[0] -= 1
                    current[1] -= 1
                    seconds += 1
                elif px > 0 > py:
                    seconds += 1
                    current[0] += 1
                    current[1] -= 1
                elif py > 0 > px:
                    seconds += 1
                    current[1] += 1
                    current[0] -= 1
        return seconds
