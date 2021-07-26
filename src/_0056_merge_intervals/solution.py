from typing import List


def solution(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    if n in (0, 1):
        return intervals
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    res = []
    x1, y1 = intervals[0]
    for x2, y2 in intervals[1:]:
        if x2 <= y1 <= y2:
            y1 = y2
        elif x1 <= x2 and y2 <= y1:
            continue
        else:
            res.append([x1, y1])
            x1, y1 = x2, y2
    res.append([x1, y1])
    return res
