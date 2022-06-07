#P14267 회사 문화 1
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
# 각 인덱스에 대한 주니어
juniors = [[] for _ in range(n+1)]
dp = [0] * (n+1)

for x, y in list(enumerate(map(int, stdin.readline().split()))):
  if x == 0:
    continue
  juniors[y].append(x+1)

def DFS(x):  
  for k in juniors[x]:
    dp[k] += dp[x]
    DFS(k)
  return

for _ in range(m):
  k, w = map(int, stdin.readline().split())
  dp[k] += w

DFS(1)
print(*dp[1:])