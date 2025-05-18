#P14567. 선수과목
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
dp = [1] * (n+1)
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, stdin.readline().split())
  indegree[b] += 1
  graph[a].append(b)

q = deque()

for i in range(1, n+1):
  if indegree[i] == 0:
    q.append(i)

while q:
  x = q.popleft()
  for next in graph[x]:
    indegree[next] -= 1
    dp[next] = max(dp[next], dp[x] + 1)
    if indegree[next] == 0:
      q.append(next)

print(*dp[1:])
