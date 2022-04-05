#P12761 돌다리
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

a, b, n, m = map(int, stdin.readline().split())
visited = [False] * 100001
dx = [a, b, -a, -b, 1, -1, a, b]

def bfs():
  queue = deque()
  queue.append((n, 0))
  visited[n] = True
  
  while queue:
    x, count = queue.popleft()
    for i in range(8):
      if i < 6:
        nx = x + dx[i]
      else:
        nx = x * dx[i]
      
      if nx < 0 or nx > 100000 or visited[nx]:
        continue
      if nx == m:
        return count + 1

      visited[nx] = True
      queue.append((nx, count + 1))
  return -1

print(bfs())

