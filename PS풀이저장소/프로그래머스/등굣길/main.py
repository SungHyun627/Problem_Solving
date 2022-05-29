def solution(m, n, puddles):
    t = [tuple(i) for i in puddles]
    print(t)
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if (j+1, i+1) not in t:
                if i != 0 and j != 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
            
    return dp[n-1][m-1] % 1000000007