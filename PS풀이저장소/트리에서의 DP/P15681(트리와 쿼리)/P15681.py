#P15681 트리와 쿼리
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')
n, r, q = map(int, stdin.readline().split())
tree = [[] for _ in range(n+1)]
dp = [1] * (n+1)

# 간선 입력
for _ in range(n-1):
  a, b = map(int, stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)

# 방문 트리
visited = [False] * (n+1)
def dfs(x):
  visited[x] = True
  for i in tree[x]:
    if not visited[i]:
      dfs(i)
      dp[x] += dp[i]

dfs(r)
for _ in range(q):
  print(dp[int(stdin.readline())])