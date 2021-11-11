#P11660 구간 합 구하기 5
from sys import stdin

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = board[i-1][j-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] += dp[i][j-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] += dp[i-1][j]

for _ in range(m):
    a, b, c, d = map(int, stdin.readline().split())
    result = dp[c][d] - dp[c][b-1] - dp[a-1][d] + dp[a-1][b-1]
    print(result)