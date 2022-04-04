#P11048 이동하기
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if i == 0:
      if j == 0:
        dp[i][j] = board[i][j]
        continue
      dp[i][j] = dp[i][j-1] + board[i][j]
    else:
      if j == 0:
        dp[i][j] = board[i][j] + dp[i-1][j]
      else:
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + board[i][j]

print(dp[n-1][m-1])
