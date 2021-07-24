def solution(x: float, n: int) -> float:
        
    def helper(p):
        if p == 0:
            return 1
        if p % 2 == 0:
            temp = helper(p // 2)
            return temp * temp
        else:
            return x * helper(p - 1)
    
    res = helper(abs(n))
    return res if n >= 0 else 1 / res
