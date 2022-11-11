#P1562 계단 수
from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
dp = [[ [0] * (2 ** 10) for _ in range(10)] for _ in range(n+1)]
t = int(1e9)
result = 0
for i in range(1, 10):
  dp[1][i][1 << i] = 1

for i in range(2, n+1):
  for j in range(10):
    for k in range(1 << 10):
      if (k & (1 << j)):
        if j != 9:
          dp[i][j][k] += (dp[i-1][j+1][k & ~(1 << j)] + dp[i-1][j+1][k])
        if j != 0:
          dp[i][j][k] += (dp[i-1][j-1][k & ~(1 << j)] + dp[i-1][j-1][k])
        dp[i][j][k] %= t
            
for i in range(10):
  result += dp[n][i][(1 << 10) - 1]
result %= t
print(result)
