from typing import List


def solution(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j = m - 1, n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
