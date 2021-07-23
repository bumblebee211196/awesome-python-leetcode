from typing import List

INF = float("inf")


def solution(nums1: List[int], nums2: List[int]) -> float:
    n, m = len(nums1), len(nums2)
    if n > m:
        nums1, nums2 = nums2, nums1
        n, m = m, n
    total = n + m
    half = total // 2
    l, r = 0, n - 1
    while True:
        i = (l + r) // 2
        j = half - i - 2
        l1 = nums1[i] if i >= 0 else -INF
        r1 = nums1[i + 1] if i + 1 < n else INF
        l2 = nums2[j] if j >= 0 else -INF
        r2 = nums2[j + 1] if j + 1 < m else INF
        if l1 <= r2 and l2 <= r1:
            if total % 2 == 1:
                return min(r1, r2)
            return (max(l1, l2) + min(r1, r2)) / 2
        if l1 > r2:
            r = i - 1
        else:
            l = i + 1
