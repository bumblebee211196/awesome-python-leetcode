def solution(s: str) -> bool:
    braces_map = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for char in s:
        if stack and stack[-1] in braces_map and braces_map[stack[-1]] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0
