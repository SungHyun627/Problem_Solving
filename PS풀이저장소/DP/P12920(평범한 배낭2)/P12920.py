##P12920. 평범한 배낭 2
from sys import stdin
stdin = open('./input.txt', 'r')

def split_items(w, c, cnt):
  result = []
  k = 1
  while cnt > 0:
    amount = min(k, cnt)
    result.append((w*amount, c*amount))
    cnt -= amount
    k *= 2
  return result

n, m = map(int, stdin.readline().split())

dp = [0] * (m+1)
items = []

for _ in range(n):
  w, c, k = map(int, stdin.readline().split())
  results = []
  items.extend(split_items(w, c, k))

for i in range(1, len(items)+1):
  w, v = items[i-1]
  for j in range(m, w-1, -1):
    dp[j] = max(dp[j], dp[j-w] + v)

print(dp[m])