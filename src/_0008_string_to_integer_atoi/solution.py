MAX = 2 ** 31


def solution(s: str) -> int:
    negative = None
    number = 0
    s = s.strip()
    for _, c in enumerate(s):
        if c == "+" and negative is None:
            negative = False
        elif c == "-" and negative is None:
            negative = True
        elif 48 <= ord(c) <= 57:
            if negative is None:
                negative = False
            number = number * 10 + int(c)
        else:
            break
    if negative is None:
        negative = False
    number = -number if negative else number
    if number > MAX - 1:
        number = MAX - 1
    if number < -MAX:
        number = -MAX
    return number
