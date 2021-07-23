def solution(n: int) -> str:
    pattern = '11'
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    for _ in range(n-2):
        count = 1
        temp = ""
        for i in range(len(pattern)-1):
            if pattern[i] == pattern[i+1]:
                count += 1
            else:
                temp += f"{count}{pattern[i]}"
                count = 1
        temp += f"{count}{pattern[-1]}"
        pattern = temp
    return pattern
