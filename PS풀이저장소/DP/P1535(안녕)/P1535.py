## P1535.안녕
from sys import stdin
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
weights = list(map(int, stdin.readline().split()))
costs = list(map(int, stdin.readline().split()))

dp = [0] * 100

for i in range(n):
  w = weights[i]
  c = costs[i]
  for j in range(99, w-1, -1):
    dp[j] = max(dp[j], dp[j-w] + c)
  
print(dp[99])
