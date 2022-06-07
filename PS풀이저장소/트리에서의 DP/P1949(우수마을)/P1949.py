#P1949 우수마을
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
tree = [[] for _ in range(n+1)]
people = [0] + list(map(int, stdin.readline().split()))
dp = [[people[i], 0] for i in range(n+1)]
# print(dp)

for _ in range(n-1):
  a, b = map(int, stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)

# 방문리스트
visited = [False] * (n+1)
def dfs(x):
  visited[x] = True
  for i in tree[x]:
    if not visited[i]:
      dfs(i)
      dp[x][0] += dp[i][1]
      dp[x][1] += max(dp[i])
  # print(x, dp)

dfs(1)
print(max(dp[1])) 