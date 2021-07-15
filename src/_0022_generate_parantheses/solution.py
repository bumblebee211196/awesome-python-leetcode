from typing import List


def solution(n: int) -> List[str]:
    
    def helper(l, r, res):
        if l + r == 2 * n:
            ans.append("".join(res))
        if l < n:
            res.append("(")
            helper(l + 1, r, res)
            res.pop()
        if l > r:
            res.append(")")
            helper(l, r + 1, res)
            res.pop()
    
    ans = []
    helper(0, 0, [])
    return ans
