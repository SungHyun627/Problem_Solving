#P2293 동전 1
from sys import stdin

stdin = open('./input.txt')
n, k = map(int, stdin.readline().split())
coins = []

dp = [0] * (k+1)
dp[0] = 1
for _ in range(n):
  coins.append(int(stdin.readline()))
coins.sort()

for i in range(n):
  for j in range(coins[i], k+1):
    dp[j] += dp[j-coins[i]]

print(dp[-1])