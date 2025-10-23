def solution(m, n, puddles):
    MOD = 1_000_000_007
    counts = [[0 for i in range(n)] for j in range(m)]
    counts[0][0] = 1
    for i in range(m):
        for j in range(n):
            if [i + 1, j + 1] in puddles:
                counts[i][j] = 0
                continue
            if i - 1 >= 0:
                counts[i][j] += (counts[i - 1][j])% MOD
            if j - 1 >= 0:
                counts[i][j] += (counts[i][j - 1])% MOD
    return (counts[m - 1][n - 1])% MOD