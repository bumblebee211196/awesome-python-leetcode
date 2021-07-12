from typing import List


def solution(strs: List[str]) -> str:
    if not strs:
        return ""
    for i, cgroup in enumerate(zip(*strs)):
        if len(set(cgroup)) > 1:
            return strs[0][:i]
    return min(strs)
