from typing import List


MAPPER = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def solution(digits: str) -> List[str]:
    
    def helper(digits: List[str], res):
        if not digits:
            return res
        if not res:
            res = MAPPER[digits[0]]
        else:
            t = []
            for v in res:
                for c in MAPPER[digits[0]]:
                    t.append(f"{v}{c}")
            res = t
        return helper(digits[1:], res)
    
    return helper(list(digits), [])
