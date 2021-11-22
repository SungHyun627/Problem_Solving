#P1890 점프
from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = list([0]*n for _ in range(n))
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j]:
            if not board[i][j]:
                continue
            if j + board[i][j] <= n-1:
                dp[i][j + board[i][j]] += dp[i][j]
            if i + board[i][j] <= n-1:
                dp[i+board[i][j]][j] += dp[i][j]
            # print(i, j, dp)

# print(dp)
print(dp[n-1][n-1])
            