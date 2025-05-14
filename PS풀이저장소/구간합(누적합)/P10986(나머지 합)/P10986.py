### P10986 나머지 합
from sys import stdin
from collections import defaultdict
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
arr = [0]+list(map(int ,stdin.readline().split()))
ans = 0
d = defaultdict(int)

for i in range(1, n+1):
  arr[i] %= m
for i in range(1, n+1):
  arr[i] = (arr[i] + arr[i-1])%m
  d[arr[i]]+=1

for key, value in d.items():  
  ans += (value * (value-1) // 2)
  if key == 0:
    ans += value

print(ans)