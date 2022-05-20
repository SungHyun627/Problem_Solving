#P2644 촌수계산
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
x, y = map(int, stdin.readline().split())
m = int(stdin.readline())

result = -1
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(k, count):
  global result
  if k == y:
    result = count
    return
  
  for i in graph[k]:
    if not visited[i]:
      visited[i] = True
      dfs(i, count+1)
  return

visited[x] = True
dfs(x, 0)
print(result)