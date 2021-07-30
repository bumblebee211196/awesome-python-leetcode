from typing import List


def solution(n: int, k: int) -> List[List[int]]:
    def helper(idx, curr):
        if len(curr) == k:
            nonlocal res
            res.append(curr[:])
            return
        for i in range(idx, n + len(curr) - k + 2):
            curr.append(i)
            helper(i + 1, curr)
            curr.pop()

    res = []
    helper(1, [])
    return res
