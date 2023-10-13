#P16928 뱀과 사다리 게임
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
snakes = [0] * 101
ladders = [0] * 101
visited = [False] * 101

for _ in range(n):
  x, y = map(int, stdin.readline().split())
  ladders[x] = y
for _ in range(m):
  x, y = map(int, stdin.readline().split())
  snakes[x] = y

def bfs():
  q = deque([])
  q.append((1, 0))
  visited[1] = True

  while q:
    cur, num = q.popleft()
    for i in range(1, 7):
      next = cur + i
      if next > 100 or visited[next]:
        continue
      if next == 100:
        return num + 1
      lower_next, upper_next = snakes[next], ladders[next]
      visited[next] = True
      if not lower_next and not upper_next:
        q.append((next, num + 1))
      elif lower_next:
        if not visited[lower_next]:
          q.append((lower_next, num + 1))
          visited[lower_next] = True
      else :
        q.append((upper_next, num + 1))
        visited[upper_next] = True        

print(bfs())