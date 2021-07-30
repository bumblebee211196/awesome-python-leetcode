def solution1(word1: str, word2: str) -> int:
    def helper(i, j):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        if (i, j) in memo:
            return memo[i, j]
        if word1[i] == word2[j]:
            res = helper(i + 1, j + 1)
        else:
            res = 1 + min(helper(i + 1, j + 1), helper(i + 1, j), helper(i, j + 1))
        memo[i, j] = res
        return res

    memo = {}
    return helper(0, 0)


def solution2(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = i
            elif i == 0:
                dp[i][j] = j
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]
