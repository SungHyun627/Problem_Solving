### P27361 막대 자르기
from sys import stdin
stdin = open('./input.txt', 'r')
t = int(stdin.readline())
INF = float('inf')

for _ in range(t):
  n, k, a, b = map(int, stdin.readline().rstrip().split())
  arr = list(map(int, stdin.readline().split()))
  cnt_one = arr.count(1)
  req = k - cnt_one
  
  if req <= 0:
    print(0)
    continue
  
  max_len = req+max(arr)

  dp = [INF] * (max_len+1)
  dp[0] = 0
  
  for s in arr:
    if s == 1:
      continue
    cost =  a * (s-1) ** 2 + b
    for x in range(max_len, s-1, -1):
      dp[x] = min(dp[x], dp[x-s] + cost)
  print(min(dp[req:]))