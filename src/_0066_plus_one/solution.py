from typing import List


def solution(digits: List[int]) -> List[int]:
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        carry, r = divmod(digits[i] + carry, 10)
        digits[i] = r
    if carry > 0:
        digits = [carry] + digits
    return digits
