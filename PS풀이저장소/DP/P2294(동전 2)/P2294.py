#P2294 동전 2
from sys import stdin

stdin = open('./input.txt', 'r')
n, k = map(int, stdin.readline().split())
dp = [10001] * (k+1)
dp[0] = 0

arr = []
for _ in range(n):
  arr.append(int(stdin.readline()))

for i in range(1, k+1):
  for j in range(n):
    if (i - arr[j]) >= 0:
      dp[i] = min(dp[i], dp[i-arr[j]] + 1)
if dp[-1] == 10001:
  print(-1)
else:
  print(dp[-1])