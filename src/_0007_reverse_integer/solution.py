def solution(x: int) -> int:
    abs_x = abs(x)
    new_num = 0
    j = len(str(abs_x)) - 1
    while abs_x != 0:
        new_num += (abs_x % 10) * (10 ** j)
        abs_x = abs_x // 10
        j -= 1
    if new_num < 2147483647:
        if x < 0:
            new_num = new_num * -1
        return new_num
    return 0
