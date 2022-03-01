#P1932 정수 삼각형
from sys import stdin
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
dp = [[0] * n for _ in range(n)]

for i in range(n):
  temp = list(map(int, stdin.readline().split()))
  if i == 0:
    dp[0][0] = temp[0]
  else:
    for j in range(i+1):
      if j == 0:
        dp[i][j] = dp[i-1][0] + temp[0]
      elif j == i:
        dp[i][j] = dp[i-1][j-1] + temp[j]
      else:
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + temp[j]
print(max(dp[n-1]))