from typing import List


def solution(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix[0])
    for row in matrix:
        if target > row[-1]:
            continue
        else:
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
