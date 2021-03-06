from typing import List


def solution(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    x, y = newInterval
    if not intervals:
        return [[x, y]]
    new_intervals = []
    i = 0
    for i, (x_, y_) in enumerate(intervals):
        if x_ <= x:
            new_intervals.append([x_, y_])
        else:
            break
    new_intervals.append([x, y])
    for i in range(i, len(intervals)):
        new_intervals.append(intervals[i])

    intervals = []
    for x, y in new_intervals:
        if not intervals or intervals[-1][1] < x:
            intervals.append([x, y])
        else:
            intervals[-1][1] = max(intervals[-1][1], y)
    return intervals
