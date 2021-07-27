def solution(a: str, b: str) -> str:
    a = list(map(int, list(a)))
    b = list(map(int, list(b)))
    res = []
    la, lb = len(a), len(b)
    i, j = la - 1, lb - 1
    carry = 0
    while i >= 0 and j >= 0:
        carry, r = divmod(a[i] + b[j] + carry, 2)
        res.append(r)
        i -= 1
        j -= 1
    while i >= 0:
        carry, r = divmod(a[i] + carry, 2)
        res.append(r)
        i -= 1
    while j >= 0:
        carry, r = divmod(b[j] + carry, 2)
        res.append(r)
        j -= 1
    if carry > 0:
        res.append(carry)
    return "".join(list(map(str, res[::-1])))
