from typing import List


def solution(arr: List[int]) -> int:
    n = len(arr)
    if n < 3:
        return 0
    total = 0
    i, j = 0, n - 1
    l_max, r_max = arr[i], arr[j]
    while i <= j:
        if l_max < r_max:
            total += l_max - arr[i]
            i += 1
        else:
            total += r_max - arr[j]
            j -= 1
        l_max, r_max = max(l_max, arr[i]), max(r_max, arr[j])
    return total
