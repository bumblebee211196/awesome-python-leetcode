from typing import List
from collections import defaultdict


def solution(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        res[key].append(word)
    return list(res.values())
