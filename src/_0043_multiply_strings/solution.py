def solution(num1: str, num2: str) -> str:
    if "0" in (num1, num2):
        return "0"
    n1, n2 = len(num1), len(num2)
    if 1 in (n1, n2):
        num2, num1 = sorted([num1, num2], key=len)
        carry = 0
        res = []
        for v1 in num1[::-1]:
            carry, r = divmod(int(v1) * int(num2) + carry, 10)
            res.append(str(r))
        if carry > 0:
            res.append(str(carry))
        return "".join(res)[::-1]
    num2, num1 = sorted([num1, num2], key=len)
    carry = 0
    res = []
    for v1 in num1[::-1]:
        carry, r = divmod(int(solution(v1, num2)) + carry, 10)
        res.append(str(r))
    if carry > 0:
        res.append(str(carry)[::-1])
    return "".join(res)[::-1]
