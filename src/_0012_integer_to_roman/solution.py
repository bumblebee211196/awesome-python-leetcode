def solution(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = []
    for v, r in zip(values, roman):
        res.append((num // v) * r)
        num %= v
    return "".join(res)
