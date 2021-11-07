#P2688 줄어들지 않아
from sys import stdin

stdin = open('./input.txt', 'r')
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    #i번째 자리(0~n-1)에 j가 올 경우의 수,
    dp = [[0] * 10 for _ in range(n)]
    for i in range(10):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(10):
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]
    
    print(sum(dp[n-1]))