def solution(path: str) -> str:
    paths = path.split("/")
    stack = []
    for p in paths:
        if p in ("", "."):
            continue
        elif p == "..":
            if stack:
                stack.pop()
        else:
            stack.append(p)
    return "/" + "/".join(stack)
