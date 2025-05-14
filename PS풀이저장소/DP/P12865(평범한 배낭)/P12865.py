from sys import stdin
stdin = open('./input.txt', 'r')

### 1차원 배열
n, k = map(int, stdin.readline().split())
weights = []
values = []

for _ in range(n):
  a, b = map(int, stdin.readline().split())
  weights.append(a)
  values.append(b)

dp = [0] * (k+1)

for i in range(1, n+1):
  w = weights[i-1]
  v = values[i-1]

  for j in range(k, w-1, -1):
    dp[j] = max(dp[j], dp[j-w] + v)
print(dp[k])



### 2차원 배열
n, k = map(int, stdin.readline().split())
weights = []
values = []

for _ in range(n):
  a, b = map(int, stdin.readline().split())
  weights.append(a)
  values.append(b)

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
  w = weights[i-1]
  v = values[i-1]

  for j in range(k+1):
    if j < w:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] +v)

print(dp[n][k])