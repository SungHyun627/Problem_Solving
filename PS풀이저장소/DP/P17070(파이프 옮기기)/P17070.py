#P17070 파이프 옮기기
from sys import stdin
stdin = open('./input.txt', 'r')
n = int(stdin.readline())
board = list(list(map(int, stdin.readline().split())) for _ in range(n))

#0 : 가로, #1: 세로, #2: 대각선
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

dp[0][1][0]= 1

def oob(x, y):
  return x < 0 or y < 0 or x >= n or y >= n

for i in range(n):
  for j in range(n):
    if board[i][j]:
      continue
    #가로 방향
    if not oob(i, j-1):
      if not oob(i, j-2):
        dp[i][j][0] += dp[i][j-1][0]
      if not oob(i-1, j-2):
        dp[i][j][0] += dp[i][j-1][2]
    #세로 방향
    if not oob(i-1, j):
      if not oob(i-2, j):
        dp[i][j][1] += dp[i-1][j][1]
      if not oob(i-2, j-1):
        dp[i][j][1] += dp[i-1][j][2]
    #대각선 뱡향
    if not oob(i-1, j-1) and not board[i-1][j] and not board[i][j-1]:
      if not oob(i-1, j-2):
        dp[i][j][2] += dp[i-1][j-1][0]
      if not oob(i-2, j-1):
        dp[i][j][2] += dp[i-1][j-1][1]
      if not oob(i-2, j-2):
        dp[i][j][2] += dp[i-1][j-1][2]
print(sum(dp[n-1][n-1]))